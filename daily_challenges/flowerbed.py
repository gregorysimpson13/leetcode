# Runtime: O(n); beats 29%
# Space: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        if len(flowerbed) < 3: return sum(flowerbed) == 0 and n < 2
        for i in range(len(flowerbed)):
            if not i and not flowerbed[i] and not flowerbed[i+1]: flowerbed[i] = 1; n = n - 1
            elif i == len(flowerbed) - 1 and not flowerbed[i] and not flowerbed[i-1]: flowerbed[i] = 1; n = n - 1
            elif not flowerbed[i] and not flowerbed[i-1] and not flowerbed[i+1]: flowerbed[i] = 1; n = n - 1;
            if n <= 0: return True
        return False