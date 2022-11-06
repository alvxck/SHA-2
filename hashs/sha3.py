# SHA-3 Algorithms 
# -----------------------------------------------------------------------------------------------------

def sha3_224(message):
    '''Converts message to binary and hashes message using SHA3-224.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '01'
    return sponge(message, 224, 1600-448)

def sha3_256(message):
    '''Converts message to binary and hashes message using SHA3-256.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '01'
    return sponge(message, 256, 1600-512)

def sha3_384(message):
    '''Converts message to binary and hashes message using SHA3-384.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '01'
    return sponge(message, 384, 1600-768)

def sha3_512(message):
    '''Converts message to binary and hashes message using SHA3-512.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '01'
    return sponge(message, 512, 1600-1024)

def shake128(message, length):
    '''Converts message to binary and hashes message using SHAKE128.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '1111'
    return sponge(message, 256, length)

def shake256(message, length):
    '''Converts message to binary and hashes message using SHAKE256.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    message = ''.join([format(ord(char), '08b') for char in message]) + '1111'
    return sponge(message, 512, length)

# KECCAK-f[b] and Intermediate functions
# -----------------------------------------------------------------------------------------------------

def keccak(S):
    '''Helper function to perform KECCAK permutations on a given message.
    Returns a 1600-bit string modified by KECCAK permutations [θ, p, π, χ, and i]

    Parameters:
    S : str 
        string of 1600-bits used to describe a message.

    '''

    w = 64
    l = 6

    # 1. State Array Construction
    def state_initialize():
        '''Initializes state array based on {S}'''
        a = {}

        for y in range(0, 5):
            for x in range(0, 5):
                for z in range(0, w):
                    a[x, y, z] = int(S[w * (5*y + x) + z])
        
        return a

    # 2. Keccak-p Permutations
    # θ (Algorithm 1)
    def θ(a):
        '''Modifies a given state array {a} based on Keccak-p (θ) permutations.'''

        c = {}

        for x in range(0, 5):
            for z in range(0, w):
                c[x, z] = a[x, 0, z] ^ a[x, 1, z] ^ a[x, 2, z] ^ a[x, 3, z] ^ a[x, 4, z]

        d = {}

        for x in range(0, 5):
            for z in range(0, w):
                d[x, z] = c[(x-1) % 5, z] ^ c[(x+1) % 5, (z-1) % w]

        a_ = {}

        for y in range(0, 5):
            for x in range(0, 5):
                for z in range(0, w):
                    a_[x, y, z] = a[x, y, z] ^ d[x, z]

        return a_

    # p (Algorithm 2)
    def p(a):
        '''Modifies a given state array {a} based on Keccak-p (p) permutations.'''

        a_ = {}
        (x, y) = (1, 0)

        for z in range(0, w):
            a_[0, 0, z] = a[0, 0, z]
        
        for t in range(0, 24):
            for z in range(0, w):
                a_[x, y, z] = a[x, y, (z-(t+1)*(t+2)//2) % w]
            (x, y) = (y, (2*x + 3*y) % 5)

        return a_

    # π (Algorithm 3)
    def π(a):
        '''Modifies a given state array {a} based on Keccak-p (π) permutations.'''

        a_ = {}

        for y in range(0, 5):
            for x in range(0, 5):
                for z in range(0, w):
                    a_[x, y, z] = a[(x + 3*y) % 5, x, z]

        return a_

    # χ (Algorithm 4)
    def χ(a):
        '''Modifies a given state array {a} based on Keccak-p (χ) permutations.'''

        a_ = {}

        for y in range(0, 5):
            for x in range(0, 5):
                for z in range(0, w):
                    a_[x, y, z] = a[x, y, z] ^ ((a[(x+1) % 5, y, z] ^ 1) & a[(x+2) % 5, y, z])
        
        return a_

    # rc (Algorithm 5)
    def rc(t):
        '''Initializes a round constant.'''

        if t % 255 == 0:
            return 1

        r = [1, 0, 0, 0, 0, 0, 0, 0]

        for i in range(1, (t % 255)+1):
            r.insert(0, 0)
            r[0] = r[0] ^ r[8] 
            r[4] = r[4] ^ r[8] 
            r[5] = r[5] ^ r[8] 
            r[6] = r[6] ^ r[8]
            r.pop()
        
        return r[0]

    # ι (Algorithm 6)
    def i(A, r):
        '''Modifies a given state array {A} based ona round constant {rc} '''

        a_ = A
        rc_ = [0 for x in range(0, w)]

        for j in range(0, l+1):
            rc_[(2**j) - 1] = rc(j + (7*r))

        for z in range(0, w):
            a_[0, 0, z] = a_[0, 0, z] ^ rc_[z]

        return a_

    # Rnd  
    def Rnd(A, r):
        '''Peform all KECCAK permutations on state array {A}.'''

        return i(χ(π(p(θ(A)))), r)

    # 3. State Array Decomposition
    a = state_initialize()

    for r in range(0, 24):
        a = Rnd(a, r)

    s_ = ''

    for y in range(0, 5):
        for x in range(0, 5):
            for z in range(0, w):
                s_ += str(a[x, y, z])

    return s_


# pad10*1 
# ----------------------------------------------------------------------------------------------------- 
def pad(x, m):
    '''Pad data with 0's until it is a multiple of x.
    
    Parameters
    ----------
    message : str 
        message to be hashed.
            
    '''

    j = (-m-2) % x

    return '1' + '0'*j + '1'


# sponge construction
# ----------------------------------------------------------------------------------------------------- 
def sponge(message, bit_length, rate):
    '''Helper function to perform absorbtion and squeezing steps of KECCAK. 
    Returns Digest of message based on bit_length and rate.

    Parameters:
    message : str 
        message to be hashed.
    bit_length : int
        length of digest.
    rate : int 
        hash rate of specified algorithm.

    '''

    # 1. Set Constants
    p = message + pad(rate , len(message))
    n = len(p)//rate
    c = 1600 - rate
    s = '0'
    p_ = {}
    z = ''

    # 2. Absorb
    for i in range(0, n):
        p_[i] =  p[i*rate:(i*rate)+rate]
        s = keccak(format(int(s, 2) ^ int(p_[i] + '0'*c, 2), '01600b'))

    # 3. Squeeze
    z = s[0:rate] 

    if bit_length >= int(z, 2):
        s = keccak(format(int(s, 2), '01600b'))
        z += s[0:rate]
    else:
        return format(int(z[0:bit_length], 2), 'x')
