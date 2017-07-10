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

def create_list_integer_range(end):
    """
    Return a list of integer
    Create a list of all integer possible between 0 to the max integer returned
    by find_index_range()

    Parameters
    ----------
    end : integer
        The max index number to create the list based on range

    Returns
    -------
    list
        A list of all integer from 0 to range(end+1)
    """
    integer_list = []
    #add end+1 to get end in list
    for i in range(end+1):
        integer_list.append(i)
    return integer_list

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
        expected_output = list(range(10+1))
        self.assertEqual(
                expected_output, create_list_integer_range(index_range))

    def test_create_list_of_integer_range_with_3_words(self):
        """
        Test create a list of integer from index range
        """
        list_index = get_list_index(self.three_words)
        index_range = find_index_range(list_index)
        expected_output = list(range(210+1))
        self.assertEqual(
                expected_output, create_list_integer_range(index_range))

    def test_create_list_of_integer_range_with_5_words(self):
        """
        Test create a list of integer from index range
        """
        list_index = get_list_index(self.five_words)
        index_range = find_index_range(list_index)
        expected_output = list(range(43210+1))
        self.assertEqual(
                expected_output, create_list_integer_range(index_range))

if __name__ == '__main__':
    unittest.main()
