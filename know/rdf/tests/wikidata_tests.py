import unittest
from rdf.parser.sparql_reader import read


class ReadTest(unittest.TestCase):
    """ Sample test case """
    def setUp(self):
        # You can optionally setup things here that can be used in the rest of the tests
        pass

    def test_read_replaces_0(self):
        """ Typical test name format is like test_thing_in_situation_does_thing
            e.g., test_invalid_uri_does_raise_error
        """

        # arrange
        expected = ("SELECT ?label{\n"
          "  wd:Q41513 p:P31 [ps:P31 ?instanceOf].\n"
          "  ?instanceOf rdfs:label ?label\n"
          "  FILTER((LANG(?label)) = \"en\")\n}\n")

        # act
        actual = read("get_instance.sparql", "Q41513")

        # assert
        self.assertEqual(expected, actual)
