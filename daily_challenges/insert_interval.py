#Runtime: O(n); beats 72.13%
#Space: O(n); beats 66.83%
​#Leetcode Hard... took me some time

from typing import List
from bisect import insort_left


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or not intervals[0]: return [newInterval]
        insort_left(intervals, newInterval)
        result = []
        prev_left, prev_right = intervals[0]
        for i, (left, right) in enumerate(intervals[1:], 1):
            if prev_right < left: result.append([prev_left, prev_right]); prev_right = right; prev_left = left
            elif prev_left <= left <= prev_right: prev_right = max(right, prev_right)
            if i == len(intervals) - 1: result.append([prev_left, prev_right])
        return result