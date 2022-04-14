# SHA-2  

Python implementation of SHA-2 Cryptographic Hash Functions: 
* SHA-256
* SHA-384
* SHA-512

## Conventions

*file structure* - Each hash algorithm uses different `hashConstants`, `roundConstants`, index values, digest sizes, and calculation constraints therefor each algorithm is contained within its own class to conserve structuring. 

*strings* - Within the `hash()` method, integers are used to perform calculations although strings are used in the *Chunk Loop* to represent binary in order to combine 8-bit blocks into 32-bit blocks while preserving leading zeros.

## Hash Algorithms

### [sha256.py](https://github.com/alvxck/SHA-2/blob/master/src/sha256.py)

SHA-256 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()`: 
* Takes 1 argument: `raw_data` (string).
* Returns the 256-bit digest of raw_data in hexidecimal.
* All calculations performed in modulo 2^32.

### [sha384.py](https://github.com/alvxck/SHA-2/blob/master/src/sha384.py)

SHA-384 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()`: 
* Takes 1 argument: `raw_data` (string).
* Returns the 384-bit digest of raw_data in hexidecimal.
* All calculations performed in modulo 2^64.


### [sha512.py](https://github.com/alvxck/SHA-2/blob/master/src/sha512.py)

SHA-512 implementation in accordance with NIST **[FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)** standard.

`hash()`: 
* Takes 1 argument: `raw_data` (string).
* Returns the 512-bit digest of raw_data in hexidecimal.
* All calculations performed in modulo 2^64.

## Operations

`rotr()`: 
* Right-Rotate Bitwise Operator.
* Takes 2 arguments: `num` (int), `bits` (int).
* Returns an integer circular-shifted right by a specified number of bits.
* exp. `rotr(000111, 2)` => 110001.

## Hashing Process

1. Pre Process
    * Convert each character in `raw_data` to binary (8-bit) and concatenate each to `schedule`.
    * Add a single *1* to `schedule`.
    * Pad `schedule` with *0's* until it is a multiple of 512 (SHA-256) or a multiple of 1024 (SHA-384 / SHA-512).
    * Use the last 64-bits (SHA-256) or 128-bits (SHA-384 / SHA-512) of `schedule` to represent the length of `raw_data`.

2. Chunk Loop
    * Break `schedule` into 32-bit sections and save all sections to `blocks`.
    * Append 48 *0's* (32-bit) to `blocks`.

3. Compression Loop
    * Modify these 48 *0's* following SHA-2 hash computation procedures. 
    * SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**.
    * SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**.


4. Mutation Loop
    * Initialize all 8 `hashConstants` to a b c d e f g h respectively.
    * Modify a-h using the values in `blocks` and values in `roundConstants` following SHA-2 hash computation procedures.
    * SHA-256 **[[6.2.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=27)**.
    * SHA-384 / SHA-512 **[[6.4.2]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf#page=29)**.
    * Repeat previous step once for each value in `roundConstants`. (SHA-256: x64 iterations | SHA-384/SHA-512: x80 iterations) 

6. Concatenation
    * Concatenate all 8 newly modified values in `hashConstants` to create 256-bit / 512-bit digest for SHA-256 and SHA-512.
    * Concatenate first 6 newly modified values in `hashConstants` to create 384-bit digest for SHA-384.
    * Return `digest` to user.