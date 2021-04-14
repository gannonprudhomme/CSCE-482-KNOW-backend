from dateutil.parser import parse
from datetime import datetime

def format_date_string(date_str: str) -> str:
    """ Converts a date string like 2019-09-01T07:58:30.996+0200 into
        September 1, 2019
    """
    parsed_date = parse(date_str)
    # Windows and unix do non-leading zero dates differently, so handle both of them
    win_date_format = "%B %#d, %Y" 
    unix_date_format = "%B %-d, %Y"
    try:
        return parsed_date.strftime(unix_date_format)
    except ValueError:
        return parsed_date.strftime(win_date_format)
