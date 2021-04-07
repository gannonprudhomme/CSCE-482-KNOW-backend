import sys
sys.path.insert(1, "../parser")
import unittest
from summarizer import Summarizer
from urllib.error import HTTPError

class SummarizerTester(unittest.TestCase):
    """summarizer test case """
    def setUp(self):
        # You can optionally setup things here that can be used in the rest of the tests
        pass

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
        """ Tests if summarizer finds Albert Einstein's wikidata URI.
        """

        # arrange
        expected = 'http://www.wikidata.org/entity/Q937'

        # act
        summer = Summarizer('http://viaf.org/viaf/75121530098098/') #invalid URI
        

        # assert
        self.assertRaises(HTTPError, summer.get_wikidata_uri)

tester = SummarizerTester()
tester.test_summarizer_finds_wikidata_uri()
tester.test_summarizer_raises_exception_for_bad_uri()