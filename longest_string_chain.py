# 1048. Longest String Chain - MEDIUM

# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.

 

# Example 1:

# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

# Note:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

def longestStrChain(words) -> int:
    words.sort(key=lambda x: len(x))
    words_map = {}
    global_max = 1
    for word in words:
        result = 0
        for i in range(len(word)):
            substring = word[:i] + word[i+1:]
            if substring in words_map:
                result = max(result, words_map[substring] + 1, 1)
        words_map[word] = result if result > 0 else 1
        global_max = max(result, global_max)
    print (words_map)
    return global_max


print(longestStrChain(["a","b","ba","bca","bda","bdca"]), 4)