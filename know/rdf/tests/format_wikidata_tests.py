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
                            "value": "sovereign state in North Africa and Asia"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Egypt"
                        },
                        "population": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "94798827"
                        },
                        "areaKmSquared": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "1010407.87"
                        },
                        "headOfGov": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q54901515"
                        },
                        "headOfState": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q307871"
                        },
                        "continentLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Africa"
                        },
                        "capitalLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Cairo"
                        },
                        "headOfGovLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Moustafa Madbouly"
                        },
                        "headOfStateLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Abdel Fattah el-Sisi"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "sovereign state in North Africa and Asia"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Egypt"
                        },
                        "population": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "94798827"
                        },
                        "areaKmSquared": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "1010407.87"
                        },
                        "headOfGov": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q54901515"
                        },
                        "headOfState": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q307871"
                        },
                        "continentLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Asia"
                        },
                        "capitalLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Cairo"
                        },
                        "headOfGovLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Moustafa Madbouly"
                        },
                        "headOfStateLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Abdel Fattah el-Sisi"
                        }
                    }
                ]
            }
        }

        expected = {
            "title": "Egypt",
            "subtitle": "sovereign state in North Africa and Asia",
            "entries": {
                "Population": [
                    {
                        "value": "94,798,827"
                    },
                ],
                "Continent": [
                    {
                        "value": "Africa"
                    },
                    {
                        "value": "Asia"
                    }
                ],
                "Capital": [
                    {
                        "value": "Cairo"
                    },
                ],
                "Area": [
                    {
                        "value": "1,010,407 km sq."
                    },
                ],
                "Head of Government": [
                    {
                        "value": "Moustafa Madbouly",
                        "link": "http://www.wikidata.org/entity/Q54901515"
                    },
                ],
                "Head of State": [
                    {
                        "value": "Abdel Fattah el-Sisi",
                        "link": "http://www.wikidata.org/entity/Q307871"
                    },
                ]
            }
        }

        result = format_country(json_input)

        # assert
        self.assertEqual(result, expected)
