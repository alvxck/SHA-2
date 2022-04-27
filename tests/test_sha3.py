import unittest
from hashs.sha3 import *

class TestSHA224(unittest.TestCase):
    def test_sha_224(self):
        self.assertEqual(sha3_224('hello world'), 'dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5')

    def test_sha_256(self):
        self.assertEqual(sha3_256('hello world'), '644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938')

    def test_sha_284(self):
        self.assertEqual(sha3_384('hello world'), '83bff28dde1b1bf5810071c6643c08e5b05bdb836effd70b403ea8ea0a634dc4997eb1053aa3593f590f9c63630dd90b')

    def test_sha_512(self):
        self.assertEqual(sha3_512('hello world'), '840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a')

if __name__ == '__main__':
    unittest.main()