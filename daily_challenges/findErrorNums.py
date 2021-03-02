class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        a0 = a1 = None
        for i in range(1,len(nums)+1):
            if i not in count: a1 = i
            if count[i] > 1: a0 = i
        return a0, a1