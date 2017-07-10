import unittest

def get_list_index(seq):
    list_index = []
    for i in range(len(seq)):
        list_index.append(i)
    return list_index

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

if __name__ == '__main__':
    unittest.main()
