# 953. Verifying an Alien Dictionary - EASY
# https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


def isAlienSorted(words, order) -> bool:
    order_dict = {}
    for counter, value in enumerate(list(order)):
        order_dict[value] = counter
    for word_i in range(len(words)-1):
        # always compare the next one
        left_word = words[word_i]
        right_word = words[word_i+1]
        for letter_i in range(max(len(left_word), len(right_word))):
            if letter_i >= len(right_word):
                return False
            if letter_i >= len(left_word):
                break
            if order_dict[left_word[letter_i]] > order_dict[right_word[letter_i]]:
                return False
            if order_dict[left_word[letter_i]] < order_dict[right_word[letter_i]]:
                break
    return True


print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
print(isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"), False)
print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)
print(isAlienSorted(["abs","apple","app","jump"], "abcdefghijklmnopqrstuvwxyz"), False)
print(isAlienSorted(["abs","app","apple","jump"], "abcdefghijklmnopqrstuvwxyz"), True)