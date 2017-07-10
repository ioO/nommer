import unittest
import random

def get_list_index(seq):
    """
    Return a list of index corresponding to the number of index in seq

    Parameters
    ----------
    seq : list
        A list of words

    Returns
    -------
    List
        A list of integer that represent index of seq
    """
    list_index = []
    for i in range(len(seq)):
        list_index.append(i)
    return list_index

def find_index_range(seq):
    """
    Return an integer representing the max integer of index list

    Parameters
    ----------
    seq : list
        A list of words

    Returns
    -------
    int
    """
    seq.reverse()
    return int(''.join(str(el) for el in seq))

def create_list_integer_range(end, fill):
    """
    Return a list of string of number
    Create a list of all integer possible between 0 to the max integer returned
    by find_index_range() and convert each value to string

    Parameters
    ----------
    end : integer
        The max index number to create the list based on range
    fill : integer
        A len to fill the number with leading 0

    Returns
    -------
    list
        A list of all integer from 0 to range(end+1)
    """
    integer_list = []
    #add end+1 to get end in list
    for i in range(end+1):
        integer_list.append(str(i).zfill(fill))
    return integer_list

def create_possible_index_string(list_index, all):
    """
    Create a list of string that represent a sequence of index

    Parameters
    ----------
    list_index : list
        List of index number we want
    all : list
        List of integer from a range

    Returns
    -------
    list
        A list of string that represent a sequence of integer which contains
        all index in list_index
    """
    result = []
    for possible_index in all:
        tmp_result = []
        for i in list_index:
            tmp_result.append(str(i) in possible_index)
        if False not in tmp_result:
            result.append(possible_index)
    return result

def create_possible_index(seq):
    """
    Create a list of index for all possible combination

    Parameters
    ----------
    seq : list
        List of all index in string

    Returns
    -------
    list
        Each item of contain a list of index
    """
    result = []
    for i in seq:
        result.append(list(int(i) for i in list(i)))

    return result

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


if __name__ == '__main__':
    unittest.main()
