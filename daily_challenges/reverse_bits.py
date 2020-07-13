class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1
            result = result + (n & 1)
            n >>= 1
        return result


# 00000010100101000001111010011100
# print(bin(Solution().reverseBits(11)), bin(11)) #1011 -> 1101
# print(bin(Solution().reverseBits(21)), bin(21))

numbers = [43261596]
for num in numbers:
    print(bin(Solution().reverseBits(num)), bin(num))
