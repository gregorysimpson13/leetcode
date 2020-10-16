# Runtime: O(log n)
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            vert = (top + bottom) // 2
            left, right = 0, len(matrix[vert]) - 1
            while left <= right:
                horiz = (left + right) // 2
                if matrix[vert][horiz] == target: return True
                elif matrix[vert][horiz] < target: left = horiz + 1
                elif matrix[vert][horiz] > target: right = horiz - 1
            if matrix[vert][0] < target: top = vert + 1
            elif matrix[vert][0] > target: bottom = vert - 1
        return False
