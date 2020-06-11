# 796. Rotate String - EASY
# https://leetcode.com/problems/rotate-string/

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true

# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:

# A and B will have length at most 100.

def rotateString(A:str, B: str) -> bool:
    if len(A) != len(B): return False
    for i in range(len(A)):
        for j in range(len(B)):
            math = (i + j) % (len(A))
            #print(j, B[j], math, A[math])
            if B[j] != A[math]:
                break
            if j == len(B) - 1:
                return True
    return False

print(rotateString('abcde', 'cdeab'), True)
print(rotateString('abcde', 'cdeab'), True)
print(rotateString('abcde', 'abced'), False)
print(rotateString('a', 'a'), True)
print(rotateString('ae', 'ae'), True)
print(rotateString('ea', 'ae'), True)
