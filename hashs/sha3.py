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

def shake128(message):
    pass

def shake256(message):
    pass

# KECCAK-f[b] and Sponge Intermediates
# -----------------------------------------------------------------------------------------------------

def keccak():
    w = 64
    l = 6

    # 1. State Array Construction
    def state_initialize():
        A = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A[x, y, z] = w * (5*y + x) + z
        
        return A

    # 2. Keccak-p Permutation
    # k0 specification (θ)
    def θ(A):
        C = {}

        for x in range(0, 5):
            for z in range(0, w):
                C[x, z] = A[x, 0, z] ^ A[x, 1, z] ^ A[x, 2, z] ^ A[x, 3, z] ^ A[x, 4, z]

        D = {}

        for x in range(0, 5):
            for z in range(0, w):
                D[x, z] = C[(x-1) % 5, z] ^ C[(x+1) % 5, (z-1) % w]

        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[x, y, z] = A[x, y, z] ^ D[x, z]

        return A_

    # k1 specification (p)
    def p(A):
        A_ = {}
        (x, y) = (1, 0)

        for z in range(0, w):
            A_[0, 0, z] = A[0, 0, z]
        
        for t in range(0, 24):
            for z in range(0, w):
                A_[x, y, z] = A[x, y, (z-(t+1)*(t+2)//2) % w]
            (x, y) = (y, (2*x + 3*y) % 5)

        return A_

    # k2 specification (π)
    def π(A):
        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[x, y, z] = A[(x + 3*y) % 5, x, z]

        return A_

    # k3 specification (χ)
    def χ(A):
        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[x, y, z] = A[x, y, z] ^ ((A[(x+1) % 5, y, z] ^ 1) & A[(x+2) % 5, y, z])
        
        return A_

    # k4 specification (rc)
    def rc(t):
        R = [1, 0, 0, 0, 0, 0, 0, 0]

        for i in range(1, t % 255):
            R.insert(0, 0)
            R[0] = R[0] ^ R[8] 
            R[4] = R[4] ^ R[8] 
            R[5] = R[5] ^ R[8] 
            R[6] = R[6] ^ R[8]
            R.pop()
        
        return R[0]

    # k5 specification (ι)
    def i(A, r):
        A_ = A
        RC = [0 for x in range(0, w)]

        for j in range(0, l):
            RC[(2**j) - 1] = rc(j + (7*r))

        for z in range(0, w):
            A_[0, 0, z] = A_[0, 0, z] ^ RC[z]

        return A_

    # k6 specification (rnd)
    def Rnd(A, r):
        return i(χ(π(p(θ(A)))), r)

    # 3. State Array Decomposition
    A = state_initialize()

    for r in range(0, 24):
        A = Rnd(A, r)

    return A


def sponge(bit_length, message):
    #1. Pre-Process 'message'
    k = keccak()

    #2. Truncate Loop
    