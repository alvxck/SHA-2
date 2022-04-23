import unittest
from sha2.sha384 import *

class TestSHA384(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA384()
        self.assertEqual(case1.hash('hello world'), 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd')

        # case 2: multi-block test
        case2 = SHA384()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '146b481a1f3a61b1fb59e88d3b4b0ee964cbcafb862ae56c5ee94da72fb715c20187ebcca51414bdf50f95dfa4a812bf')



if __name__ == '__main__':
    unittest.main()