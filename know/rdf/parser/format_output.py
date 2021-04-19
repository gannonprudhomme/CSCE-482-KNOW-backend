from typing import Union, List
from collections import defaultdict
from dateutil.parser import parse

def format_output(
    title: str, subtitle: str, description: Union[str, None], entries: List[dict]
) -> dict:
    """ Standardizes the response that is sent to the frontend. Should be called in the
        parse_book, parse_person, etc. functions

        Note that each entry in the entries array should have a key-value pair with key
        'key' and key 'value', e.g. {'key': 'Birth Date', 'value': 'September 8th, 1998'}
    """
    data = {
        'title': title,
        'subtitle': subtitle,
        'entries': entries
    }

    if description: # Only add description if it's not None
        data['description'] = description

    return data

def format_date_string(date_str: str) -> str:
    """ Converts a date string like 2019-09-01T07:58:30.996+0200 into
        September 1, 2019
    """
    parsed_date = parse(date_str)
    if date_str[0] == '-':
        return f"{parsed_date.year} BCE"

    # Windows and unix do non-leading zero dates differently, so handle both of them
    win_date_format = "%B %#d, %Y"
    unix_date_format = "%B %-d, %Y"
    try:
        return parsed_date.strftime(unix_date_format)
    except ValueError:
        return parsed_date.strftime(win_date_format)

def _get_value_or_none(data: dict, key: str) -> str:
    """ Returns the value for the given key if it exists. If it doesn't, returns None """
    entry = data.get(key)
    if entry:
        return entry.get('value')

    return None

def _detected_duplicate(val: str, pretty_key: str, entries: dict) -> bool:
    """ Checks if there is already an entry with this key and value in entries """
    if pretty_key in entries:
        # Skip if we've already entered this value
        for existing_entry in entries[pretty_key]:
            if existing_entry["value"] == val:
                return True

    return False

def format_query(
    response: dict, entries_translations: dict, entries_links: dict,
    special_format: type(lambda val, key: str),
) -> dict:
    """ Given the response (from Wikidata), formats the data into the output expected by
        the frontend.
        Uses `entries_translations` to determine how to format the human-readable
        name for the corresponding keys.

        Uses `entries_links` to determine the translation between a label column and its
        corresponding entity id column (e.g. "headOfGovLabel": "headOfGov")

        `special_format` is a function that is called once a value is retrieved form a
        column and allows the function caller to optionally format the value, e.g. if one
        wanted to format a date into a human-readable format.
    """

    data = response['results']['bindings']
    # Defaultdict makes it so we don't have to create a new list for each key -
    # if the key doesn't exist when we try to insert into it, it automatically makes
    # an empty one for us
    entries = defaultdict(list)

    for entry in data:
        name = _get_value_or_none(entry, "name")
        subtitle = _get_value_or_none(entry, "description")

        for key, pretty_key in entries_translations.items():
            val = _get_value_or_none(entry, key)

            if special_format: # If there's a special_format function provided
                val = special_format(val, key)

            if not val: # guard statement
                continue

            # First, check if there's a link corresponding for this value
            link_col_name = entries_links.get(key)
            link = None
            if link_col_name:
                link = _get_value_or_none(entry, link_col_name)

            if _detected_duplicate(val, pretty_key, entries): # Skip duplicates
                continue

            if link: # if there's a link, add it
                entries[pretty_key].append({ "value": val, "link": link })
            else:
                # If we can't, just enter the value
                entries[pretty_key].append({ "value": val })

    return format_output(name, subtitle, None, dict(entries))
