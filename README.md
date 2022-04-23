# SHA

Python implementation of SHA-2 and SHA-3 Cryptographic Hash Algorithms.

**SHA-2:** sha224 | sha256 | sha384 | sha512

**SHA-3:** sha3-224 | sha3-256 | sha3-384 | sha3-512

<!-- *What is SHA?*-->


## Conventions

*file structure* - Each hash algorithm is contained within its own class since different `hash_constants`, `round_constants`, index values, digest sizes, and calculation constraints are used for each. 

*strings* - All calculations are performed with integers however strings are used to preserving leading zeros when concatenating bits.

## SHA-2 Hash Algorithms

Implementations in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()` : 
* Takes 1 argument: `message` *string*.
* Returns the hash digest of `message`.

### [sha224.py](https://github.com/alvxck/SHA-2/blob/master/sha2/sha224.py)
```
test = SHA224()
test.hash('hello world')

> '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b'
```

### [sha256.py](https://github.com/alvxck/SHA-2/blob/master/sha2/sha256.py)
```
test = SHA256()
test.hash('hello world')

> 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
```

### [sha384.py](https://github.com/alvxck/SHA-2/blob/master/sha2/sha384.py)
```
test = SHA384()
test.hash('hello world')

> 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd'
```

### [sha512.py](https://github.com/alvxck/SHA-2/blob/master/sha2/sha512.py)
```
test = SHA512()
test.hash('hello world')

> '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
```

`rotr()` : 
* Right-Rotate Bitwise Operator.
* Takes 2 arguments: `num` *int*, `bits` *int*.
* Returns an integer circular-shifted right by a specified number of bits.

ex.
```
rotr(8, 2)

# 8 => 0b1000 => 0b10 => 2
> 2
```

## SHA-2 Hashing Process

1. Pre Process
    * Convert each character in `message` to binary (8-bit) and concatenate each to `data`.
    * Add a single *1* to `data`.
    * Pad `data` with *0's* until it is a multiple of 512-bits (SHA224 / SHA-256) or a multiple of 1024-bits (SHA-384 / SHA-512).
    * Use the last 64-bits (SHA224 / SHA-256) or 128-bits (SHA-384 / SHA-512) of `data` to represent the length of `message`.

2. Chunk Loop
    * Break `data` into 32-bit (SHA224 / SHA-256) or 64-bit (SHA-384 / SHA-512) sections and save all sections to `blocks`.
    * Append 48 *0's* (SHA224 / SHA-256) or 80 *0's* (SHA-384 / SHA-512) to `blocks`.

3. Compression Loop
    * Modify the *0's* added in step 2 following SHA-2 hash computation procedures.  
    (SHA-224 / SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**. SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**)

4. Mutation Loop
    * Initialize all 8 `hash_constants` to a b c d e f g h respectively.
    * Modify a-h using the values in `blocks` and values in `round_constants` following SHA-2 hash computation procedures.  
    (SHA-224 / SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**. SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**)
    * Repeat previous step once for each value in `round_constants`.  
    (SHA-224 / SHA-256: x64 iterations | SHA-384 / SHA-512: x80 iterations)

6. Concatenation
    * Concatenate newly modified values in `hash_constants` to create digest.
    * Return `digest` to user.

<!-- SHA3 -->

## SHA-3 Hash Algorithms

Implementations in accordance with NIST **[FIPS PUB 202](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)** standard.

`hash()` : 
* Takes 1 argument: `message` *string*.
* Returns the hash digest of `message`.

### [sha3_224.py](https://github.com/alvxck/SHA-2/blob/master/sha3/sha3_224.py)
```
test = SHA3_224()
test.hash('hello world')

> 'dfb7f18c77e928bb56faeb2da27291bd790bc1045cde45f3210bb6c5'
```

### [sha3_256.py](https://github.com/alvxck/SHA-2/blob/master/sha3/sha3_256.py)
```
test = SHA3_256()
test.hash('hello world')

> '644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938'
```

### [sha3_384.py](https://github.com/alvxck/SHA-2/blob/master/sha3/sha3_384.py)
```
test = SHA3_384()
test.hash('hello world')

> '83bff28dde1b1bf5810071c6643c08e5b05bdb836effd70b403ea8ea0a634dc4997eb1053aa3593f590f9c63630dd90b'
```

### [sha3_512.py](https://github.com/alvxck/SHA-2/blob/master/sha3/sha3_512.py)
```
test = SHA3_512()
test.hash('hello world')

> '840006653e9ac9e95117a15c915caab81662918e925de9e004f774ff82d7079a40d4d27b1b372657c61d46d470304c88c788b3a4527ad074d1dccbee5dbaa99a'
```

## SHA-3 Hashing Process

