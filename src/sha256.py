

class SHA256:
    def __init__(self):
        self.hashConstants = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19 ]
        self.roundConstants = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2 ]
        
    def hash(self, raw_data):
        # 1. Pre-Process 'raw_data'
        data = [ord(char) for char in raw_data]

        data.append(128)

        while (len(data) % 64 != 0):
            data.append(0)
        
        schedule = ''.join([format(num, '08b') for num in data])

        if '1' in schedule[-64:]:
            schedule += format(8*len(raw_data), '0512b')
        else:
            schedule = schedule[:-64] + format(8*len(raw_data), '064b')

        # 2. Chunk Loop
        blocks = []

        for x in range(0, len(schedule) // 512):
            blocks.append([schedule[x*512:(x*512)+512]])
            blocks[x] = [int(blocks[x][0][y:y+32], 2) for y in range(0, len(blocks[x][0]), 32)]
            blocks[x].extend([0]*48) 

        # 3. Compression Loop
        for block in range(0, len(blocks)):
            for entry in range(16, 64):
                s0 = (rotr(blocks[block][entry-15], 7)) ^ (rotr(blocks[block][entry-15], 18)) ^ (blocks[block][entry-15] >> 3)
                s1 = (rotr(blocks[block][entry-2], 17)) ^ (rotr(blocks[block][entry-2], 19)) ^ (blocks[block][entry-2]>> 10)
                blocks[block][entry] = (blocks[block][entry-16] + s0 + blocks[block][entry-7] + s1) % 2**32
    
        # 4. Mutation Loop
        for block in range(0, len(blocks)):
            a, b, c, d, e, f, g, h = self.hashConstants

            for entry in range(0, 64):
                s0 = (rotr(e, 6)) ^ (rotr(e, 11)) ^ (rotr(e, 25))
                ch = (e & f) ^ (~e & g)
                temp1 = (h + s0 + ch + self.roundConstants[entry] + blocks[block][entry]) % 2**32
                s1 = (rotr(a, 2)) ^ (rotr(a, 13)) ^ (rotr(a, 22))
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (s1 + maj) % 2**32

                h = g
                g = f
                f = e
                e = (d + temp1) % 2**32
                d = c
                c = b
                b = a
                a = (temp1 + temp2) % 2**32

            self.hashConstants[0] = (self.hashConstants[0] + a) % 2**32
            self.hashConstants[1] = (self.hashConstants[1] + b) % 2**32
            self.hashConstants[2] = (self.hashConstants[2] + c) % 2**32
            self.hashConstants[3] = (self.hashConstants[3] + d) % 2**32
            self.hashConstants[4] = (self.hashConstants[4] + e) % 2**32
            self.hashConstants[5] = (self.hashConstants[5] + f) % 2**32
            self.hashConstants[6] = (self.hashConstants[6] + g) % 2**32
            self.hashConstants[7] = (self.hashConstants[7] + h) % 2**32

        # 5. Digest Concatenation
        digest = ''.join([format(hash, 'x') for hash in self.hashConstants])

        return digest

# Right-Rotate Bitwise Operator. [exp. rotr('000111', 2) -> '110001']
def rotr(num, bits):
    x = format(num, '032b')
    return int(x[-bits:] + x[:len(x)-bits], 2)
