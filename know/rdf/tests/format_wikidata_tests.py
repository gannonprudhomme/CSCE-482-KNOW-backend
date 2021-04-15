from unittest import TestCase
from rdf.parser.wikidata_formatter import format_landmark, format_country

class FormatWikidataTests(TestCase):
    """ Tests the wikidata formatter functions """
    def setUp(self):
        self.maxDiff = None # pylint: disable=invalid-name

    def test_format_landmark(self):
        """ Tests format_landmark """
        # arrange
        json_input = {
            "head": {
                "vars": [
                    "name",
                    "description",
                    "territoryLocation",
                    "territoryLocationLabel",
                    "countryLocation",
                    "countryLocationLabel",
                    "inception",
                    "coordinates"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "tower located on the Champ de Mars in Paris, France"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Eiffel Tower"
                        },
                        "territoryLocation": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q259463"
                        },
                        "countryLocation": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q142"
                        },
                        "territoryLocationLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "7th arrondissement of Paris"
                        },
                        "countryLocationLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "France"
                        },
                        "inception": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1887-01-28T00:00:00Z"
                        },
                        "coordinates": {
                            "datatype": "http://www.opengis.net/ont/geosparql#wktLiteral",
                            "type": "literal",
                            "value": "Point(2.294479 48.858296)"
                        }
                    }
                ]
            }
        }
        expected = {
            "title": "Eiffel Tower",
            "subtitle": "tower located on the Champ de Mars in Paris, France",
            "entries": {
                "Territory": [
                    {
                        "value": "7th arrondissement of Paris",
                        "link": "http://www.wikidata.org/entity/Q259463",
                    },
                ],
                "Country": [
                    {
                        "value": "France",
                        "link": "http://www.wikidata.org/entity/Q142"
                    }
                ],
                "Creation Date": [
                    {
                        "value": "January 28, 1887"
                    }
                ]
            }
        }

        # act
        result = format_landmark(json_input)
        print(repr(expected))
        print(repr(result))

        # assert
        self.assertEqual(result, expected)

    def test_format_country(self):
        """ Tests format_country """
        json_input ={
            "head": {
                "vars": [
                    "name",
                    "description",
                    "population",
                    "continentLabel",
                    "capitalLabel",
                    "areaKmSquared",
                    "headOfGov",
                    "headOfGovLabel",
                    "headOfState",
                    "headOfStateLabel"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "country in Western Europe"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "France"
                        },
                        "population": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "66628000"
                        },
                        "areaKmSquared": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "643801"
                        },
                        "headOfGov": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q3171170"
                        },
                        "headOfState": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q3052772"
                        },
                        "continentLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Europe"
                        },
                        "capitalLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Paris"
                        },
                        "headOfGovLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Jean Castex"
                        },
                        "headOfStateLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Emmanuel Macron"
                        }
                    }
                ]
            }
        }

        expected ={
            "title": "France",
            "subtitle": "country in Western Europe",
            "entries": {
                "Population": [
                    {
                        "value": "66628000"
                    }
                ],
                "Continent": [
                    {
                        "value": "Europe"
                    }
                ],
                "Capital": [
                    {
                        "value": "Paris"
                    }
                ],
                "Area": [
                    {
                        "value": "643801 km sq."
                    }
                ],
                "Head of Government": [
                    {
                        "value": "Jean Castex",
                        "link": "http://www.wikidata.org/entity/Q3171170"
                    }
                ],
                "Head of State": [
                    {
                        "value": "Emmanuel Macron",
                        "link": "http://www.wikidata.org/entity/Q3052772"
                    }
                ]
            }
        }

        result = format_country(json_input)

        # assert
        self.assertEqual(result, expected)
