# Runtime: O(n); beats 87.75
# Space: O(n)
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        ans, i = [], len(nums) - 1
        while num:
            if nums[i] <= num: ans.append(roman[i]); num -= nums[i]
            else: i -= 1
        return "".join(ans)