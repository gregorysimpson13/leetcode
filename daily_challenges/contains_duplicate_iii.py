
# Runtime: O(n**2)
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[i] - nums[j]) <= t: return True
        return False


# Runtime: Beats 16%
# Space: Beats 9%
from collections import defaultdict
class Buckets:
    def __init__(self, min_num, max_num, t):
        self.min_num, self.max_num, self.t = min_num, max_num, t+1
        self.buckets = defaultdict(list)
    def add(self, num):
        index = self.__get_index(num)
        if len(self.buckets[index]): return True
        self.buckets[index].append(num)
        if index - 1 >= 0 and self.buckets[index-1] and abs(max(self.buckets[index-1]) - num) <= (self.t-1): return True
        if self.buckets[index+1] and abs(min(self.buckets[index+1]) - num) <= (self.t-1): return True
        return False
    def remove(self, num):
        index = self.__get_index(num)
        self.buckets[index].remove(num)
    def __get_index(self, num):
        return (num-self.min_num) // self.t

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        k = k+1
        if len(nums) <= 1: return False
        if t < 0: return False
        bucket = Buckets(min(nums), max(nums), t)
        for i, val in enumerate(nums):
            if i-k >= 0: bucket.remove(nums[i-k])
            if bucket.add(val): return True
        return False