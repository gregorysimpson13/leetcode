# 1222. Queens That Can Attack the King
# https://leetcode.com/problems/queens-that-can-attack-the-king/submissions/


from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result_list = []
        queens_set = set([(row, col) for row, col in queens])
        for row, col in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]:
            curr_row, curr_col = king[0] + row, king[1] + col
            while curr_row >= 0 and curr_row < 8 and curr_col >= 0 and curr_col < 8:
                if (curr_row, curr_col) in queens_set:
                    result_list.append([curr_row, curr_col])
                    break
                curr_row += row; curr_col += col
        return result_list