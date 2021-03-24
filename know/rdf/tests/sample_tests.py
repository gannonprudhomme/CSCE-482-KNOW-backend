import unittest

def some_function(val):
    """ some basic function """
    return val

class SampleTestCase(unittest.TestCase):
    """ Sample test case """
    def setUp(self):
        # You can optionally setup things here that can be used in the rest of the tests
        pass

    def test_sample_test_returns_5(self):
        """ Typical test name format is like test_thing_in_situation_does_thing
            e.g., test_invalid_uri_does_raise_error
        """

        # arrange
        expected = 5

        # act
        actual = some_function(expected)

        # assert
        self.assertEqual(expected, actual)
