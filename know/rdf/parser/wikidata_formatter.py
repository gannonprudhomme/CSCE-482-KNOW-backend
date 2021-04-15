from collections import defaultdict
from rdf.parser.format_output import format_output
from rdf.utils import format_date_string

def get_value_or_none(data: dict, key: str) -> str:
    """ Returns the value for the given key if it exists. If it doesn't, returns None """
    entry = data.get(key)
    if entry:
        return entry.get('value')

    return None

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

        `special_format` is a function that is called once a value is retrieved form a column
        and allows the function caller to optionally format the value, e.g. if one
        wanted to format a date into a human-readable format.
    """

    data = response['results']['bindings']
    # Defaultdict makes it so we don't have to create a new list for each key -
    # if the key doesn't exist when we try to insert into it, it automatically makes
    # an empty one for us
    entries = defaultdict(list)

    for entry in data:
        name = get_value_or_none(entry, "name")
        subtitle = get_value_or_none(entry, "description")

        for key, pretty_key in entries_translations.items():
            val = get_value_or_none(entry, key)

            if special_format: # If there's a special_format function provided
                val = special_format(val, key)

            if val: # If there was a corresponding value for this key
                # First, check if there's a link corresponding for this value
                link_col_name = entries_links.get(key)
                link = None
                if link_col_name:
                    link = get_value_or_none(entry, link_col_name)

                if link: # if there's a link, add it
                    entries[pretty_key].append({ "value": val, "link": link })
                else:
                    # If we can't, just enter the value
                    entries[pretty_key].append({ "value": val })

    return format_output(name, subtitle, None, dict(entries))

def format_country(response: dict) -> dict:
    """ Formats a country into the expected output format """
    entries_translations = {
        "population": "Population",
        "continentLabel": "Continent",
        "capitalLabel": "Capital",
        "areaKmSquared": "Area",
        "headOfGovLabel": "Head of Government",
        "headOfStateLabel": "Head of State"
    }

    entries_links = {
        "headOfGovLabel": "headOfGov",
        "headOfStateLabel": "headOfState"
    }

    def format_area(val: str, key: str) -> str:
        # If the key is the area, add the units
        if val and key == "areaKmSquared":
            return f"{val} km sq."

        # for all other keys, leave them alone
        return val

    return format_query(response, entries_translations, entries_links, format_area)

def format_landmark(response: dict) -> dict:
    """ Formats a landmark into the expected output format """
    entries_translations = {
        "territoryLocationLabel": "Territory",
        "countryLocationLabel": "Country",
        "inception": "Creation Date"
    }

    entries_links = {
        "territoryLocationLabel": "territoryLocation",
        "countryLocationLabel": "countryLocation",
    }

    def format_date(val: str, key: str) -> str:
        # If the key is the inception date, format it into a date string
        if val and key == "inception":
            return format_date_string(val)

        # For all other keys, leave them alone
        return val

    return format_query(response, entries_translations, entries_links, format_date)
