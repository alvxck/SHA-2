import unittest
from sha2.sha512 import *

class TestSHA512(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA512()
        self.assertEqual(case1.hash('hello world'), '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f')

        # case 2: multi-block test
        case2 = SHA512()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), 'e4089f39011cbb0ab15ab23ecbb51052813329409e9bafa982f08fcd3e093f96c5970b5ffaf92a5ea36520f82fe798216ac680acf90a291322c97ef72acb8a60')


if __name__ == '__main__':
    unittest.main()