import unittest
from sha3.sha3_512 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA3_512()
        self.assertEqual(case1.hash('hello world'), '840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a')

        # case 2: multi-block test
        case2 = SHA3_512()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '085f46efc714f5238e510c7e4192031c17f5f3b5c4c98e6d6a9e9a3606ea28a1e53bc5640bca25ad48d7a2955b8e32e1d4e32593e5b4168be1540ba9d91f771e')


if __name__ == '__main__':
    unittest.main()