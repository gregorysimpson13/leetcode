# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.


def letterCombinations(digits: str):
    if digits == "": return []
    letters_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8:'tuv', 9:'wxyz'}
    def combinations(s, i):
        if len(digits) == len(s):
            return [s]
        if i >= len(digits):
            return None
        letters = letters_dict[int(digits[i])]
        result = []
        for letter in letters:
            local_result = combinations(s + letter, i + 1)
            if local_result != None:
                result += local_result
        return result
    return combinations("", 0)

print(letterCombinations("234"))
print(letterCombinations(""))