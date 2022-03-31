from operations import *

class SHA256:
    def __init__(self, data):
        self.data = data
        self.blocks = []
        self.hashConstants = [
            '01101010000010011110011001100111', '10111011011001111010111010000101', '00111100011011101111001101110010', '10100101010011111111010100111010',
            '01010001000011100101001001111111', '10011011000001010110100010001100', '00011111100000111101100110101011', '01011011111000001100110100011001']
        self.roundConstants = [
            '01000010100010100010111110011000', '01110001001101110100010010010001', '10110101110000001111101111001111', '11101001101101011101101110100101', 
            '00111001010101101100001001011011', '01011001111100010001000111110001', '10010010001111111000001010100100', '10101011000111000101111011010101', 
            '11011000000001111010101010011000', '00010010100000110101101100000001', '00100100001100011000010110111110', '01010101000011000111110111000011',
            '01110010101111100101110101110100', '10000000110111101011000111111110', '10011011110111000000011010100111', '11000001100110111111000101110100',
            '11100100100110110110100111000001', '11101111101111100100011110000110', '00001111110000011001110111000110', '00100100000011001010000111001100',
            '00101101111010010010110001101111', '01001010011101001000010010101010', '01011100101100001010100111011100', '01110110111110011000100011011010',
            '10011000001111100101000101010010', '10101000001100011100011001101101', '10110000000000110010011111001000', '10111111010110010111111111000111', 
            '11000110111000000000101111110011', '11010101101001111001000101000111', '00000110110010100110001101010001', '00010100001010010010100101100111', 
            '00100111101101110000101010000101', '00101110000110110010000100111000', '01001101001011000110110111111100', '01010011001110000000110100010011', 
            '01100101000010100111001101010100', '01110110011010100000101010111011', '10000001110000101100100100101110', '10010010011100100010110010000101', 
            '10100010101111111110100010100001', '10101000000110100110011001001011', '11000010010010111000101101110000', '11000111011011000101000110100011', 
            '11010001100100101110100000011001', '11010110100110010000011000100100', '11110100000011100011010110000101', '00010000011010101010000001110000', 
            '00011001101001001100000100010110', '00011110001101110110110000001000', '00100111010010000111011101001100', '00110100101100001011110010110101', 
            '00111001000111000000110010110011', '01001110110110001010101001001010', '01011011100111001100101001001111', '01101000001011100110111111110011', 
            '01110100100011111000001011101110', '01111000101001010110001101101111', '10000100110010000111100000010100', '10001100110001110000001000001000', 
            '10010000101111101111111111111010', '10100100010100000110110011101011', '10111110111110011010001111110111', '11000110011100010111100011110010']
        self.digest = ''
        
    def hash(self):
        rawData = ''

        # Convert each character in 'self.data' to binary. Save to 'rawData' string.
        for char in self.data:
            rawData += format(ord(char), '08b')

        # Add a single '1' to 'rawData' and pad with 0's until it is a multiple of 512.
        rawData += '1'

        while (len(rawData) % 512 != 0):
            rawData += '0'
        
        # If any of the last 64-bits in 'rawData' are a '1' append 512 0's to 'rawData'. Modify the last 64-bits of 'rawData' to represent the length of 'data' in binary.
        if '1' in rawData[-64:]:
            rawData += format(8*len(self.data), '0512b')
        else:
            rawData = rawData[:-64] + format(8*len(self.data), '064b') 
            
        # Break 'rawData' into 512-bit blocks consisting of 32-bit entries and append 48 '00000000000000000000000000000000' to the end of each block. Save blocks to 'self.blocks' array.
        for x in range(0, len(rawData) // 512):
            self.blocks.append([rawData[x*512:(x*512)+512]])
            self.blocks[x] = [self.blocks[x][0][y:y+32] for y in range(0, len(self.blocks[x][0]), 32)]
            self.blocks[x].extend(['00000000000000000000000000000000']*48) 

        # Modify the 48 '00000000000000000000000000000000' within each block using official SHA-256 bitwise operations.
        for block in range(0, len(self.blocks)):
            for entry in range(16, 64):
                s0 = XOR([ROTR(self.blocks[block][entry-15], 7), ROTR(self.blocks[block][entry-15], 18), RSHIFT(self.blocks[block][entry-15], 3)])
                s1 = XOR([ROTR(self.blocks[block][entry-2], 17), ROTR(self.blocks[block][entry-2], 19), RSHIFT(self.blocks[block][entry-2], 10)])
                self.blocks[block][entry] = MOD32([self.blocks[block][entry-16], s0, self.blocks[block][entry-7], s1])
        
        # Initialize and Modify (a-h) once for each entry within each block inside the 'self.blocks' array using official SHA-256 bitwise operations.
        for block in range(0, len(self.blocks)):
            a = self.hashConstants[0]
            b = self.hashConstants[1]
            c = self.hashConstants[2]
            d = self.hashConstants[3]
            e = self.hashConstants[4]
            f = self.hashConstants[5]
            g = self.hashConstants[6]
            h = self.hashConstants[7]

            for entry in range(0, 64):
                s0 = XOR([ROTR(e, 6), ROTR(e, 11), ROTR(e, 25)])
                ch = XOR([AND([e, f]), AND([NOT(e), g])])
                temp1 = MOD32([h, s0, ch, self.roundConstants[entry], self.blocks[block][entry]])
                s1 = XOR([ROTR(a, 2), ROTR(a, 13), ROTR(a, 22)])
                maj = XOR([AND([a, b]), AND([a, c]), AND([b, c])])
                temp2 = MOD32([s1, maj])

                h = g
                g = f
                f = e
                e = MOD32([d, temp1])
                d = c
                c = b
                b = a
                a = MOD32([temp1, temp2])

            self.hashConstants[0] = MOD32([self.hashConstants[0], a])
            self.hashConstants[1] = MOD32([self.hashConstants[1], b])
            self.hashConstants[2] = MOD32([self.hashConstants[2], c])
            self.hashConstants[3] = MOD32([self.hashConstants[3], d])
            self.hashConstants[4] = MOD32([self.hashConstants[4], e])
            self.hashConstants[5] = MOD32([self.hashConstants[5], f])
            self.hashConstants[6] = MOD32([self.hashConstants[6], g])
            self.hashConstants[7] = MOD32([self.hashConstants[7], h])

        # Convert each of the modified hash constants to hex and concatenate to obtain the digest of the 'self.data'.
        for hash in self.hashConstants:
            self.digest += format(int(hash, 2), 'x') 

        return self.digest
