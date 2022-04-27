
def keccak():
    b = 1600
    w = 64
    l = 6
    n = 24

    # 1. State Array Construction

    #2. Keccak-p Permutation
    # k0 specification
    # k1 specification
    k1_offsets = {}
    # k2 specification
    # k3 specification
    # k4 specification

    # 3. State Array Decomposition

def sponge(bit_length, message):
    #1. Pre-Process 'message'
    k = keccak()

    #2. Truncate Loop


# SHA-3 Algorithms 
# -----------------------------------------------------------------------------------------------------
def sha3_224(message):
    return sponge(224, message)

def sha3_256(message):
    return sponge(256, message)

def sha3_384(message):
    return sponge(384, message)

def sha3_512(message):
    return sponge(512, message)
    