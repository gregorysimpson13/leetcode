
# 125. Valid Palindrome - EASY


# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

def isPalindrome(s: str) -> bool:
    import string
    print(string.digits)
    letters_set = set(string.ascii_letters)
    [letters_set.add(num) for num in string.digits]
    def findIndex(s, i, increment):
        while i >= 0 and i < len(s) and s[i] not in letters_set:
            i += increment
        return i
    l = findIndex(s,0,1)
    r = findIndex(s, len(s) - 1, -1)
    while l < r:
        if s[l].lower() != s[r].lower():
            return False
        print(s[l], s[r])
        l = findIndex(s, l+1, 1)
        r = findIndex(s, r-1, -1)
    return True



print(isPalindrome("A man, a plan, a canal: Panama"), True) 
print(isPalindrome("race a car"), False) 
print(isPalindrome("0P"), False) 
