import unittest
from unittest.mock import patch
import nommer_cli

class NommerCliTestCase(unittest.TestCase):
    """
    Test class for cli interface
    """
    def test_process(self):
        self.assertEqual(2, len(list(nommer_cli.process('hello,world'))))
        for el in nommer_cli.process(('hello,world')):
            self.assertIn(el,['ho', 'we'])

if __name__ == '__main__':
    unittest.main()
