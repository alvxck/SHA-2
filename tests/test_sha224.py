import unittest
from sha2.sha224 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA224()
        self.assertEqual(case1.hash('hello world'), '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b')

        # case 2: multi-block test
        case2 = SHA224()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '1da72422a9273122d0cb256a05195a1aa9db963fd0b8f96773386fa0')


if __name__ == '__main__':
    unittest.main()
    