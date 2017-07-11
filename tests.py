import unittest
import random
from nommer import *

class NommerTestCase(unittest.TestCase):
    """
    TestCase for Nommer
    """

    def setUp(self):
        self.two_words = ('hello', 'world')
        self.three_words = ('hello', 'world', 'how')
        self.five_words = ('hello', 'world', 'how', 'are', 'you')
        self.n_words = list('helloworldhowareyou')

    def test_get_combination_of_index_with_2_words(self):
        """
        Test generator that create combination of possible index
        """
        self.assertEqual(2, len(list(get_combination_of_index(2))))
        expected_output = [['0', '1'], ['1', '0']]
        self.assertEqual(expected_output, list(get_combination_of_index(2)))

    def test_get_combination_of_index_with_3_words(self):
        """
        Test generator that create combination of possible index
        """
        self.assertEqual(6, len(list(get_combination_of_index(3))))
        expected_output = [
                ['0', '1', '2'], ['0', '2', '1'],
                ['1', '0', '2'], ['1', '2', '0'],
                ['2', '0', '1'], ['2', '1', '0']
                ]
        self.assertEqual(expected_output, list(get_combination_of_index(3)))

    def test_get_combination_of_index_with_4_words(self):
        """
        Test generator that create combination of possible index
        """
        self.assertEqual(24, len(list(get_combination_of_index(4))))
        expected_output = [
                ['0', '1', '2', '3'], ['0', '1', '3', '2'],
                ['0', '2', '1', '3'], ['0', '2', '3', '1'],
                ['0', '3', '1', '2'], ['0', '3', '2', '1'],
                ['1', '0', '2', '3'], ['1', '0', '3', '2'],
                ['1', '2', '0', '3'], ['1', '2', '3', '0'],
                ['1', '3', '0', '2'], ['1', '3', '2', '0'],
                ['2', '0', '1', '3'], ['2', '0', '3', '1'],
                ['2', '1', '0', '3'], ['2', '1', '3', '0'],
                ['2', '3', '0', '1'], ['2', '3', '1', '0'],
                ['3', '0', '1', '2'], ['3', '0', '2', '1'],
                ['3', '1', '0', '2'], ['3', '1', '2', '0'],
                ['3', '2', '0', '1'], ['3', '2', '1', '0'],
                ]
        self.assertEqual(expected_output, list(get_combination_of_index(4)))

    def test_get_combination_of_index_with_5_words(self):
        """
        Test generator that create combination of possible index
        """
        self.assertEqual(120, len(list(get_combination_of_index(5))))
        expected_output = [
                ['0', '1', '2', '3', '4'], ['0', '2', '1', '3', '4'],
                ['4', '3', '2', '1', '0'], ['3', '2', '4', '0', '1'],
                ['2', '0', '4', '1', '3']
                ]
        for el in expected_output:
            self.assertIn(el, list(get_combination_of_index(5)))

    def test_combination_of_names_with_2_words(self):
        """
        Test generator that create all combination of names
        """
        self.assertEqual(
                2, len(list(get_combination_of_names(self.two_words)))
                )
        expected_output = ['ho', 'we']
        self.assertEqual(
            expected_output, list(get_combination_of_names(self.two_words))
            )

    def test_combination_of_names_with_3_words(self):
        """
        Test generator that create all combination of names
        """
        self.assertEqual(
                6, len(list(get_combination_of_names(self.three_words)))
                )
        expected_output = [
                'how', 'hor',
                'wew', 'wol',
                'her', 'hol'
                ]
        self.assertEqual(
            expected_output, list(get_combination_of_names(self.three_words))
            )

    def test_combination_of_names_with_5_words(self):
        """
        Test generator that create all combination of names
        """
        self.assertEqual(
                120, len(list(get_combination_of_names(self.five_words)))
                )
        expected_output = [
                'how',
                'hor',
                'yrwlo',
                'aould',
                'heul',
                ]
        for word in expected_output:
            self.assertIn(
                    word, list(get_combination_of_names(self.five_words))
                    )

if __name__ == '__main__':
    unittest.main()
