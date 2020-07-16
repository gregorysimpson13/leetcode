# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for words in strs:
            result_dict[tuple(sorted(words))].append(words)
        return list(result_dict.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))