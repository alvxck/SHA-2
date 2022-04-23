import unittest
from sha3.sha3_384 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA3_384()
        self.assertEqual(case1.hash('hello world'), '83bff28dde1b1bf5810071c6643c08e5b05bdb836effd70b403ea8ea0a634dc4997eb1053aa3593f590f9c63630dd90b')

        # case 2: multi-block test
        case2 = SHA3_384()
        self.assertEqual(case2.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '9e5d11fdf3bfdd07b6e452432e5e126642ef0fefad109687df4bbd7ce1c60d708fb535c9fe79228d91c5875a49e28ea5')


if __name__ == '__main__':
    unittest.main()