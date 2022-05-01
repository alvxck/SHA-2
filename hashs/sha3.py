# SHA-3 Algorithms 
# -----------------------------------------------------------------------------------------------------

def sha3_224(message):
    return sponge(message, 224, 1600-448)

def sha3_256(message):
    return sponge(message, 256, 1600-512)

def sha3_384(message):
    return sponge(message, 384, 1600-768)

def sha3_512(message):
    return sponge(message, 512, 1600-1024)

def shake128(message):
    pass

def shake256(message):
    pass

# KECCAK-f[b] and Intermediate functions
# -----------------------------------------------------------------------------------------------------

def keccak(S):
    w = 64
    l = 6

    # 1. State Array Construction
    def state_initialize():
        A = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A[y, x, z] = int(S[w * (5*x + y) + z])
        
        return A

    # 2. Keccak-p Permutation
    # k0 specification (θ)
    def θ(A):
        C = {}

        for y in range(0, 5):
            for z in range(0, w):
                C[y, z] = A[y, 0, z] ^ A[y, 1, z] ^ A[y, 2, z] ^ A[y, 3, z] ^ A[y, 4, z]

        D = {}

        for y in range(0, 5):
            for z in range(0, w):
                D[y, z] = C[(y-1) % 5, z] ^ C[(y+1) % 5, (z-1) % w]

        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[y, x, z] = A[y, x, z] ^ D[y, z]

        return A_

    # k1 specification (p).
    def p(A):
        A_ = {}
        (y, x) = (1, 0)

        for z in range(0, w):
            A_[0, 0, z] = A[0, 0, z]
        
        for t in range(0, 24):
            for z in range(0, w):
                A_[y, x, z] = A[y, x, (z-(t+1)*(t+2)//2) % w]
            (y, x) = (x, (2*y + 3*x) % 5)

        return A_

    # k2 specification (π)
    def π(A):
        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[y, x, z] = A[(y + 3*x) % 5, y, z]

        return A_

    # k3 specification (χ)
    def χ(A):
        A_ = {}

        for x in range(0, 5):
            for y in range(0, 5):
                for z in range(0, w):
                    A_[y, x, z] = A[y, x, z] ^ ((A[(y+1) % 5, x, z] ^ 1) & A[(y+2) % 5, x, z])
        
        return A_

    # k4 specification (rc)
    def rc(t):
        R = [1, 0, 0, 0, 0, 0, 0, 0]

        if t % 255 == 0:
            return 1

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

    # k6 specification (rnd).
    def Rnd(A, r):
        return i(χ(π(p(θ(A)))), r)

    # 3. State Array Decomposition
    A = state_initialize()

    for r in range(0, 24):
        A = Rnd(A, r)

    S_ = ''

    for x in range(0, 5):
        for y in range(0, 5):
            for z in range(0, w):
                S_ += str(A[y, x, z])

    return S_

# pad10*1 
# ----------------------------------------------------------------------------------------------------- 
def pad(x, m):
    j = (-m-2) % x

    return '1' + '0'*j + '1'


# sponge construction
# ----------------------------------------------------------------------------------------------------- 
def sponge(message, bit_length, rate):
    # 1. Set Constants
    P = ''.join([format(ord(char), '08b') for char in message]) + '01' + pad(rate , 8*len(message) + 2)
    n = len(P)//rate
    c = 1600 - rate
    S = '0'*1600
    P_ = {}
    Z = ''

    for s in range(0, n):
        P_[s] =  P[s*rate:(s*rate)+rate]

    # 2. 
    for i in range(0, n):
        S = keccak(format(int(S, 2) ^ int(P_[i] + '0'*c, 2), '01600b'))

    Z = S[0:rate] 

    if bit_length >= int(Z, 2):
        S = keccak(int(S, 2))
        Z += S[0:rate]
    else:
        return format(int(Z[0:bit_length], 2), 'x')

