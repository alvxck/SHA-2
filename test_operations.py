import unittest
import operations

class TestOperations(unittest.TestCase):
    def test_rotr(self):
        self.assertEqual(operations.rotr('000111', 2), '110001') 
        self.assertEqual(operations.rotr('11110000', 4), '00001111')

    def test_mod32(self):
        self.assertEquals(operations.mod32(['1', '1']), '00000000000000000000000000000010')
        self.assertEquals(operations.mod32(['01101000011001010110110001101100', '11001110111000011001010111001011', '00000000000000000000000000000000', '00000000000000000000000000000000']), '00110111010001110000001000110111')

    #**** ADD XOR / AND / NOT OPERATIONS FOR STRINGS


if __name__ == '__main__':
    unittest.main()