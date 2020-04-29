# 20. Valid Parentheses - EASY

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


def isValid(s: str) -> bool:
    d = {')': '(',
         ']': '[',
         '}': '{'}
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        if char in ')]}':
            if stack == [] or d[char] != stack.pop():
                return False
    return stack == []


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
