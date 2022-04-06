import unittest
from src.sha384 import *

class TestSHA384(unittest.TestCase):
    def test_hash(self):
        test = SHA384('hello world')
        self.assertEqual(test.hash(), 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd')

if __name__ == '__main__':
    unittest.main()