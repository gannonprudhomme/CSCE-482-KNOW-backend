import unittest
from urllib.error import HTTPError
from rdf.parser.summarizer import Summarizer

class SummarizerTester(unittest.TestCase):
    """summarizer test case """
    def test_summarizer_finds_wikidata_uri(self):
        """ Tests if summarizer finds Albert Einstein's wikidata URI.
        """

        # arrange
        expected = 'http://www.wikidata.org/entity/Q937'

        # act
        summer = Summarizer('http://viaf.org/viaf/75121530/')
        actual = summer.get_wikidata_uri()

        # assert
        self.assertEqual(expected, actual)

    def test_summarizer_raises_exception_for_bad_uri(self):
        """ Tests if summarizer raises an exception given a bad URI.
        """

        # act
        summer = Summarizer('http://viaf.org/viaf/75121530098098/') #invalid URI

        # assert
        self.assertRaises(HTTPError, summer.get_wikidata_uri)
