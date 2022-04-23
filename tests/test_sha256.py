import unittest
from sha2.sha256 import *

class TestSHA256(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA256()
        self.assertEqual(case1.hash('hello world'), 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9')

        # case 2: multi-block test
        case2 = SHA256()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), 'a511b93b6dc0854560cbff02dab131a2bf6e7fb48511b80af9e0bb72bbb9bf0e')


if __name__ == '__main__':
    unittest.main()
    