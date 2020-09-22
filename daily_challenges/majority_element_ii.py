# Runtime: O(n); beats 8.5%
# Space: O(1); beats 33.59%

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = num2 = count1 = count2 = 0
        for n in nums:
            if num1 == n: count1+=1
            elif num2 == n: count2+=1
            elif count1 == 0: count1+=1; num1 = n
            elif count2 == 0: count2+=1; num2 = n
            else: count1-=1; count2-=1
        count1 = count2 = 0
        result = []
        for n in nums:
            if n == num1: count1+=1
            elif n == num2: count2+=1
        for num, count in [(num1, count1), (num2, count2)]:
            if count > len(nums) / 3: result.append(num)
        return result
        