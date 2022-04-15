import unittest
from src.sha256 import *

class TestSHA256(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA256()
        self.assertEqual(case1.hash('hello world'), 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9')

        # case 2: multi-block test
        case2 = SHA256()
        self.assertEqual(case2.hash('In encryption, data is transformed into a secure format that is unreadable unless the recipient has a key. In its encrypted form, the data may be of unlimited size, often just as long as when unencrypted.'), '9fcdb976f1b5e4832487595c7dd0df03fd9d3ec0645f3ca845e2b60d773b7619')


if __name__ == '__main__':
    unittest.main()
    