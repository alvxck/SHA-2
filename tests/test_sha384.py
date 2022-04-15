import unittest
from src.sha384 import *

class TestSHA384(unittest.TestCase):
    def test_hash(self):
        # case 1: single block test
        case1 = SHA384()
        self.assertEqual(case1.hash('hello world'), 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd')

        # case 2: multi-block test
        case2 = SHA384()
        self.assertEqual(case2.hash('In encryption, data is transformed into a secure format that is unreadable unless the recipient has a key. In its encrypted form, the data may be of unlimited size, often just as long as when unencrypted.'), 'ac3970005c69c1c7f794f758dc0707284030710ed8f3e785c4572e8ab513265277467a2d84d5243c364fcf08dbcd2b7a')



if __name__ == '__main__':
    unittest.main()