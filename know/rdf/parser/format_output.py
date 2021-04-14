from typing import Union, Array

def format_output(
    title: str, subtitle: str, description: Union[str, None], entries: Array[dict]
) -> dict:
    """ Standardizes the response that is sent to the frontend. Should be called in the
        parse_book, parse_person, etc. functions

        Note that each entry in the entries array should have a key-value pair with key 'key' and
        key 'value', e.g. { 'key': 'Birth Date', 'value': 'September 8th, 1998' }
    """
    data = {
        'title': title,
        'subtitle': subtitle,
        'entries': entries
    }

    if description: # Only add description if it's not None
        data['description'] = description

    return data
