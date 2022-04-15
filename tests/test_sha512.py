import unittest
from src.sha512 import *

class TestSHA512(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA512()
        self.assertEqual(case1.hash('hello world'), '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f')

        # case 2: multi-block test
        case2 = SHA512()
        self.assertEqual(case2.hash('In encryption, data is transformed into a secure format that is unreadable unless the recipient has a key. In its encrypted form, the data may be of unlimited size, often just as long as when unencrypted.'), 'fc0585921d5b1720881740afc7bd0c3247c861893c19d1f124ddc9d26c9a3f9c42a479138b3c8b4ccd45853835cc21af979fa615c3692205824e31daa4fc350e')


if __name__ == '__main__':
    unittest.main()