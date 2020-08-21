# Runtime: O(n); beats 57.3
# Space: O(1): beats 58.44

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        while l < r:
            while A[l] % 2 == 0 and l < r: l = l + 1
            while A[r] % 2 != 0 and l < r: r = r - 1
            A[l], A[r] = A[r], A[l]
        return A