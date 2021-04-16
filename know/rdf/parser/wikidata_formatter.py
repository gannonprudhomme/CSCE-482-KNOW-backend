from rdf.parser.format_output import format_query, format_date_string

def format_country(response: dict) -> dict:
    """ Formats a country into the expected output format
        - France: https://www.wikidata.org/wiki/Q142
        - New Zealand: https://www.wikidata.org/wiki/Q664
        - Ghana:https://www.wikidata.org/wiki/Q117
    """
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

    def format_area_and_population(val: str, key: str) -> str:
        if val:
            if key in ("areaKmSquared", "population"):
                # Convert to float from string, then convert to int to shave off decimals
                val = int(float(val))
                # Make it comma separated string
                val = "{:,}".format(val)

            if key == "areaKmSquared": # If the key is the area, add the units
                return f"{val} km sq."

        # for all other keys, leave them alone
        return val

    return format_query(
        response, entries_translations, entries_links, format_area_and_population,
    )

def format_landmark(response: dict) -> dict:
    """ Formats a landmark into the expected output format
        - Great Pyramid of Giza: https://www.wikidata.org/wiki/Q37200
        - Taj Mahal: https://www.wikidata.org/wiki/Q9141
        - Statue of Liberty: https://www.wikidata.org/wiki/Q9202
    """
    entries_translations = {
        "territoryLocationLabel": "Territory",
        "countryLocationLabel": "Country",
        "inception": "Creation Date"
    }

    entries_links = {
        "countryLocationLabel": "countryLocation",
    }

    def format_date(val: str, key: str) -> str:
        # If the key is the inception date, format it into a date string
        if val and key == "inception":
            return format_date_string(val)

        # For all other keys, leave them alone
        return val

    return format_query(response, entries_translations, entries_links, format_date)
