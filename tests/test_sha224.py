import unittest
from src.sha224 import *

class TestSHA224(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA224()
        self.assertEqual(case1.hash('hello world'), '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b')

        # case 2: multi-block test
        case2 = SHA224()
        self.assertEqual(case2.hash('In encryption, data is transformed into a secure format that is unreadable unless the recipient has a key. In its encrypted form, the data may be of unlimited size, often just as long as when unencrypted.'), '6ac8e207a27966b0caaeb56de0788b8f955782f61ef0ed9f86ea98a5')


if __name__ == '__main__':
    unittest.main()
    