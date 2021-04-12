from typing import Union

def format_output(title: str, subtitle: str, description: Union[str, None], entries: dict) -> dict:
    """ Standardizes the response that is sent to the frontend. Should be called in the
        parse_book, parse_person, etc. functions
    """
    data = {
        'title': title,
        'subtitle': subtitle,
        'entries': entries
    }

    if description: # Only add description if it's not None
        data['description'] = description

    return data
