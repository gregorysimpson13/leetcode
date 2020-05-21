# 67. Add Binary - EASY

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


'''
current bit in str a
current bit in str b
carry bit

EDGE CASES:
overflow past last bits
'''


def addBinary(a: str, b: str) -> str:
    result = ''
    carry_bit = 0
    ai, bi = len(a) - 1, len(b) - 1
    while carry_bit != 0 or ai >= 0 or bi >= 0:
        current_sum = 0
        if ai >= 0:
            current_sum += int(a[ai])
        if bi >= 0:
            current_sum += int(b[bi])
        current_sum += carry_bit
        carry_bit = 1 if current_sum >= 2 else 0
        result = str(current_sum % 2) + result
        ai -= 1
        bi -= 1
    return result


print(addBinary("1", "0"), "1")
print(addBinary("0", "0"), "0")
print(addBinary("1", "1"), "10")
print(addBinary("11", "1"), "100")
print(addBinary("11", "11"), "110")
print(addBinary("1010", "1011"), "10101")
