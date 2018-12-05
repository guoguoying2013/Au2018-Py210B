#! usr/bin/env python 3
import unittest

class MyTests(unittest.TestCase):

    def test_tautology(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()