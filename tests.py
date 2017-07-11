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

    def test_list_of_index_with_2_words(self):
        """
        Test get_list_index return a list of index from given list of 2 words
        """
        expected_list = [0, 1]
        self.assertEqual(expected_list, get_list_index(self.two_words))

    def test_list_of_index_with_3_words(self):
        """
        Test get_list_index return a list of index from given list of 3 words
        """
        expected_list = [0, 1, 2]
        self.assertEqual(expected_list, get_list_index(self.three_words))

    def test_list_of_index_with_5_words(self):
        """
        Test get_list_index return a list of index from given list of 5 words
        """
        expected_list = [0, 1, 2, 3, 4]
        self.assertEqual(expected_list, get_list_index(self.five_words))

    def test_list_of_index_with_n_words(self):
        """
        Test get_list_index return a list of index from given list of n words
        Use a random function for each test
        """
        #random number for list
        rnum = random.randint(0,len(self.n_words))
        #split the list
        new_list = self.n_words[0:rnum]
        expected_list = list(range(rnum))
        self.assertEqual(expected_list, get_list_index(new_list))

    def test_find_index_range_with_2_words(self):
        """
        Test find index range return an integer value
        """
        list_index = get_list_index(self.two_words)
        self.assertEqual(find_index_range(list_index), 10)

    def test_find_index_range_with_3_words(self):
        """
        Test find index range return an integer value
        """
        list_index = get_list_index(self.three_words)
        self.assertEqual(find_index_range(list_index), 210)

    def test_find_index_range_with_5_words(self):
        """
        Test find index range return an integer value
        """
        list_index = get_list_index(self.five_words)
        self.assertEqual(find_index_range(list_index), 43210)

    def test_create_list_of_integer_range_with_2_words(self):
        """
        Test create a list of integer from index range
        """
        list_index = get_list_index(self.two_words)
        index_range = find_index_range(list_index)
        expected_output = list(str(i).zfill(2) for i in range(10+1))
        self.assertEqual(
                expected_output, create_list_integer_range(
                    index_range, len(list_index))
                )

    def test_create_list_of_integer_range_with_3_words(self):
        """
        Test create a list of integer from index range
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        expected_output = list(str(i).zfill(3) for i in range(210+1))
        self.assertEqual(
                expected_output, create_list_integer_range(
                    index_range, len(list_index))
                )

    def test_create_list_of_integer_range_with_5_words(self):
        """
        Test create a list of integer from index range
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        expected_output = list(str(i).zfill(5) for i in range(43210+1))
        self.assertEqual(
                expected_output, create_list_integer_range(
                    index_range, len(list_index))
                )

    def test_create_possible_indexs_string_with_2_words(self):
        """
        Test the cleaning of list of all string of integer from range to only
        a list of string of integer possible index
        """
        list_index = get_list_index(self.two_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        expected_output = ['01', '10']
        self.assertEqual(
                expected_output, create_possible_index_string(
                    list_index, all_index)
                )

    def test_create_possible_index_with_3_words(self):
        """
        Test the cleaning of list of all string of integer from range to only
        a list of string of integer possible index
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        expected_output = ['012', '021', '102', '120', '201', '210']
        self.assertEqual(
                expected_output, create_possible_index_string(
                    list_index, all_index)
                )

    def test_create_possible_index_with_5_words(self):
        """
        Test the cleaning of list of all string of integer from range to only
        a list of string of integer possible index.
        Use list contains
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        expected_output = ['01234', '02134', '43210', '32401', '20413']
        result = create_possible_index_string(list_index, all_index)
        for i in expected_output:
            self.assertIn(i, result)

    def test_create_index_with_possible_for_two_words(self):
        """
        Test creation of list of index from list of integer
        """
        list_index = get_list_index(self.two_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index = create_possible_index_string(list_index, all_index)
        expected_output = [[0, 1], [1, 0]]
        self.assertEqual(
                expected_output, create_possible_index(possible_index))

    def test_create_index_with_possible_for_3_words(self):
        """
        Test creation of list of index from list of integer
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index = create_possible_index_string(list_index, all_index)
        expected_output = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0],
                [2, 0, 1], [2, 1, 0]]
        self.assertEqual(
                expected_output, create_possible_index(possible_index))

    def test_create_index_with_possible_for_5_words(self):
        """
        Test creation of list of index from list of integer
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index = create_possible_index_string(list_index, all_index)
        expected_output = [[0, 1, 2, 3, 4], [0, 2, 1, 3, 4], [4, 3, 2, 1, 0],
                [3, 2, 4, 0, 1], [2, 0, 4, 1, 3]]
        result = create_possible_index(possible_index)
        for i in expected_output:
            self.assertIn(i, result)

    def test_create_combination_of_2_words(self):
        """
        Test create combination from index list with origin list of words
        """
        list_index = get_list_index(self.two_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
                list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        expected_output = [['hello', 'world'], ['world', 'hello']]
        self.assertEqual(expected_output,
                create_combination(self.two_words, index_combination))

    def test_create_combination_of_3_words(self):
        """
        Test create combination from index list with origin list of words
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
                list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        expected_output = [
                ['hello', 'world', 'how'], ['hello', 'how', 'world'],
                ['world', 'hello', 'how'], ['world', 'how', 'hello'],
                ['how', 'hello', 'world'], ['how', 'world', 'hello']
                ]
        self.assertEqual(expected_output,
                create_combination(self.three_words, index_combination))

    def test_create_combination_of_5_words(self):
        """
        Test create combination from index list with origin list of words
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
                list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        expected_output = [
                ['hello', 'world', 'how', 'are', 'you'],
                ['hello', 'how', 'world', 'are', 'you'],
                ['you', 'are', 'how', 'world', 'hello'],
                ['are', 'how', 'you', 'hello', 'world'],
                ['how', 'hello', 'you', 'world', 'are']
                ]
        result = create_combination(self.five_words, index_combination)
        for i in expected_output:
            self.assertIn(i, result)

    def test_create_name_with_2_words(self):
        """
        Test creation of name from a list
        """
        list_index = get_list_index(self.two_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
            list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        combination = create_combination(self.two_words, index_combination)
        expected_output = ['ho', 'we']
        # generator should return only 2 elements
        self.assertEqual(2, len(list(create_name(combination))))
        for name in create_name(combination):
            self.assertIn(name, expected_output)

    def test_create_name_with_3_words(self):
        """
        Test creation of name from a list
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
            list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        combination = create_combination(self.three_words, index_combination)
        expected_output = [
                'how', 'hor',
                'wew', 'wol',
                'her', 'hol'
                ]
        self.assertEqual(expected_output, create_name(combination))

    def test_create_name_with_5_words(self):
        """
        Test creation of name from a list
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        all_index = create_list_integer_range(index_range, len(list_index))
        possible_index_string = create_possible_index_string(
            list_index, all_index)
        index_combination = create_possible_index(possible_index_string)
        combination = create_combination(self.five_words, index_combination)
        expected_output = [
                'how',
                'hor',
                'yrwlo',
                'aould',
                'heul',
                ]
        for word in expected_output:
            self.assertIn(word, create_name(combination))



if __name__ == '__main__':
    unittest.main()
