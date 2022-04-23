import unittest
from sha3.sha3_256 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA3_256()
        self.assertEqual(case1.hash('hello world'), '644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938')

        # case 2: multi-block test
        case2 = SHA3_256()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '48e04b4717cb3bf720ad42a6e02d22d3136b45007aac9a72041576af0896be7d')


if __name__ == '__main__':
    unittest.main()