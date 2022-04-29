

def sha1(message):
   rotl = lambda num, bits : (num << bits) | (num >> (32 - bits)) % 2**32
