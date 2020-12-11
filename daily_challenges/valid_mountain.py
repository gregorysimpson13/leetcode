# Runtime: O(n); beats 57.87%
# Space: O(1)
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]: return False
        idx = 0
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]: return False
            if arr[i-1] > arr[i]: idx = i; break
        for i in range(idx, len(arr)):
            if arr[i-1] <= arr[i]: return False
        return True