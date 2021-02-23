# Runtime: O(nlogn); beats 99.31%
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if not (matrix[i][0] <= target <= matrix[i][-1]): continue
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                j = (l+r)//2
                if matrix[i][j] == target: return True
                if matrix[i][j] < target: l=j+1
                else: r=j-1
        return False