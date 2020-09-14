# Runtime O(n); beats 12.45%
# Space O(1); beats 91.88%
​
class Solution:
    def rob(self, nums: List[int]) -> int:
        house_0, house_1 = 0, 0
        for house in nums:
            house_1, house_0 = max(house_0 + house, house_1), house_1
        return house_1
