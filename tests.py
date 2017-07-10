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

    def test_list_of_index_with_2_words(self):
        """
        Test get_list_index return a list of index from given list of 2 words
        """
        words = ('hello', 'world')
        expected_list = [0, 1]
        self.assertEqual(expected_list, get_list_index(words))

    def test_list_of_index_with_3_words(self):
        """
        Test get_list_index return a list of index from given list of 3 words
        """
        words = ('hello', 'world', 'how')
        expected_list = [0, 1, 2]
        self.assertEqual(expected_list, get_list_index(words))

    def test_list_of_index_with_5_words(self):
        """
        Test get_list_index return a list of index from given list of 5 words
        """
        words = ('hello', 'world', 'how', 'are', 'you')
        expected_list = [0, 1, 2, 3, 4]
        self.assertEqual(expected_list, get_list_index(words))

    def test_list_of_index_with_n_words(self):
        """
        Test get_list_index return a list of index from given list of n words
        Use a random function for each test
        """
        #split each letter
        words = ('helloworldhowareyou')
        #random number for list
        rnum = random.randint(0,len(words))
        #split the list
        new_list = words[0:rnum]
        expected_list = list(range(rnum))
        self.assertEqual(expected_list, get_list_index(new_list))

    def test_find_index_range_with_2_words(self):
        """
        Test find index range return an integer value
        """
        words = ('hello', 'world')
        list_index = get_list_index(words)
        self.assertEqual(find_index_range(list_index), 10)

if __name__ == '__main__':
    unittest.main()
