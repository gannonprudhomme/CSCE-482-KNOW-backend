import unittest
from rdf.parser.sparql_reader import read_sparql


class ReadSparqlTests(unittest.TestCase):
    """ read_sparql tests """

    def test_read_replaces_0(self):
        """ test_read_replaces_0 will check that read_sparql will
            replace the $0 in the file with a test uri
        """

        # arrange
        expected = ("SELECT ?label{\n"
          "  wd:Q41513 p:P31 [ps:P31 ?instanceOf].\n"
          "  ?instanceOf rdfs:label ?label\n"
          "  FILTER((LANG(?label)) = \"en\")\n}\n")

        # act
        actual = read_sparql("get_instance.sparql", "Q41513")

        # assert
        self.assertEqual(expected, actual)
