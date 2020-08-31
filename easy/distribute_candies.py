# https://leetcode.com/problems/distribute-candies/submissions/

# python one liner
from typing import List
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies) // 2)