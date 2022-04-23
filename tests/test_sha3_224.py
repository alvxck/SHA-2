import unittest
from sha3.sha3_224 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA3_224()
        self.assertEqual(case1.hash('hello world'), 'dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5')

        # case 2: multi-block test
        case2 = SHA3_224()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '393173ce006f88b561093472822b4a0830abe1dfff40d5329a29ddb4')


if __name__ == '__main__':
    unittest.main()