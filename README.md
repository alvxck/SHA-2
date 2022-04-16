# SHA-2  

Python implementation of SHA-2 Cryptographic Hash Algorithms.
* SHA-256
* SHA-384
* SHA-512

## Conventions

*file structure* - Each hash algorithm uses different `hash_constants`, `round_constants`, index values, digest sizes, and calculation constraints therefore each algorithm is contained within its own class to conserve structuring. 

*strings* - The `hash()` method performs calculations with integers however strings are used within the *Chunk Loop* to represent binary in order to combine 8-bit blocks into 32-bit or 64-bit blocks while preserving leading zeros.

## Hash Algorithms

### [sha256.py](https://github.com/alvxck/SHA-2/blob/master/src/sha256.py)

SHA-256 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()` : 
* Takes 1 argument: `message` *string*.
* Returns the 256-bit digest of `message` in hexidecimal.
* All calculations performed in modulo 2^32.

exp.
```
test = SHA256()
test.hash('hello world')

> 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
```

### [sha384.py](https://github.com/alvxck/SHA-2/blob/master/src/sha384.py)

SHA-384 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()` : 
* Takes 1 argument: `message` *string*.
* Returns the 384-bit digest of `message` in hexidecimal.
* All calculations performed in modulo 2^64.

exp.
```
test = SHA384()
test.hash('hello world')

> 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd'
```

### [sha512.py](https://github.com/alvxck/SHA-2/blob/master/src/sha512.py)

SHA-512 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()` : 
* Takes 1 argument: `message` *string*.
* Returns the 512-bit digest of `message` in hexidecimal.
* All calculations performed in modulo 2^64.

exp.
```
test = SHA512()
test.hash('hello world')

> '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
```

## Operations

`rotr()`: 
* Right-Rotate Bitwise Operator.
* Takes 2 arguments: `num` *int*, `bits` *int*.
* Returns an integer circular-shifted right by a specified number of bits.

exp.
```
rotr(8, 2)

# 8 => 0b1000 => 0b10 => 2
> 2
```

## Hashing Process

1. Pre Process
    * Convert each character in `message` to binary (8-bit) and concatenate each to `data`.
    * Add a single *1* to `data`.
    * Pad `data` with *0's* until it is a multiple of 512 (SHA-256) or a multiple of 1024 (SHA-384 / SHA-512).
    * Use the last 64-bits (SHA-256) or 128-bits (SHA-384 / SHA-512) of `data` to represent the length of `message`.

2. Chunk Loop
    * Break `data` into 32-bit (SHA-256) or 64-bit (SHA-384 / SHA-512) sections and save all sections to `blocks`.
    * Append 48 *0's* (SHA-256) or 80 *0's* (SHA-384 / SHA-512) to `blocks`.

3. Compression Loop
    * Modify the *0's* added in step 2 following SHA-2 hash computation procedures.  
    (SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**. SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**)

4. Mutation Loop
    * Initialize all 8 `hash_constants` to a b c d e f g h respectively.
    * Modify a-h using the values in `blocks` and values in `round_constants` following SHA-2 hash computation procedures.  
    (SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**. SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**)
    * Repeat previous step once for each value in `round_constants`.  
    (SHA-256: x64 iterations | SHA-384/SHA-512: x80 iterations)

6. Concatenation
    * Concatenate all 8 newly modified values in `hash_constants` to create a 256-bit digest (SHA-256) or 512-bit digest (SHA-512).
    * Concatenate the first 6 newly modified values in `hash_constants` to create a 384-bit digest (SHA-384).
    * Return `digest` to user.