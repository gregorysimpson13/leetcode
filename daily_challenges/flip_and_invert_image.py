# Runtime: O(n*m); beats 53.65;
# Space: O(1)
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in range(len(A)):
            left, right = 0, len(A[row]) - 1
            while left <= right:
                A[row][left], A[row][right] = int(not A[row][right]), int(not A[row][left])
                left, right = left + 1, right - 1
        return A
