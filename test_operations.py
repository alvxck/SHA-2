import unittest
import operations

class TestOperations(unittest.TestCase):
    def test_ROTR(self):
        self.assertEqual(operations.ROTR('01101000011001010110110001101100', 4), '11000110100001100101011011000110')

    def test_MOD32(self):
        self.assertEqual(operations.MOD32(['01101000011001010110110001101100', '01101000011001010110110001101100']), '11010000110010101101100011011000')

    def test_RSHIFT(self):
        self.assertEqual(operations.RSHIFT('01101000011001010110110001101100', 4), '00000110100001100101011011000110')

    def test_AND(self):
        self.assertEqual(operations.AND(['01101000011001010110110001101100', '01101000011001010110110001101100']), '01101000011001010110110001101100')

    def test_XOR(self):
        self.assertEqual(operations.XOR(['01101000011001010110110001101100', '01101000011001010110110001101100']), '00000000000000000000000000000000')

    def test_NOT(self):
        self.assertEqual(operations.NOT('01101000011001010110110001101100'), '-1101000011001010110110001101101')

if __name__ == '__main__':
    unittest.main()
    