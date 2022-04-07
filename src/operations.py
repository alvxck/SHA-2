# All operations return the binary representation of an integer as a string.
# Return in 32-bit or 64-bit format based on length of input.

# Right-Rotate Bitwise Operator. [exp. ROTR('000111', 2) -> '110001']
def ROTR(num, bits):
    return num[-bits:] + num[:len(num)-bits]

# Add (n) numbers in an array together in modulo 2^32. [exp. MOD32(['1','1']) -> '10']
def SUM(nums):
    ans = 0
    for num in nums:
        ans += (int(num, 2) % (2**len(num)))
    return format(ans % (2**len(num)), f'0{str(len(num))}b')

# Right-Shift Bitwise Operator. [exp. RSHIFT('000111', 3) -> '000000']
def RSHIFT(num, bits):
    return format(int(num, 2) >> bits, f'0{str(len(num))}b')

# AND Bitwise Operator. [exp. AND(['1', '0', '1']) -> '0']
def AND(nums):
    ans = int(nums[0], 2)
    for num in nums[1:]:
        ans &= int(num, 2)
    return format(ans, f'0{str(len(num))}b')

# XOR Bitwise Operator. [exp. XOR(['1','0','1']) -> '0']
def XOR(nums):
    ans = int(nums[0], 2)
    for num in nums[1:]:
        ans ^= int(num, 2)
    return format(ans, f'0{str(len(num))}b')

# NOT Bitwise Operator. [exp. NOT('0') -> '1']
def NOT(num):
    return format(~int(num, 2), f'0{str(len(num)+1)}b')