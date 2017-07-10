import unittest
import random

def get_list_index(seq):
    list_index = []
    for i in range(len(seq)):
        list_index.append(i)
    return list_index

def find_index_range(seq):
    seq.reverse()
    return int(''.join(str(el) for el in seq))

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


if __name__ == '__main__':
    unittest.main()
