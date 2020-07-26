#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0,0)])
        current_y, current_x = 0, 0
        for direction in path:
            if direction == 'N': current_y = current_y + 1
            if direction == 'S': current_y = current_y - 1
            if direction == 'E': current_x = current_x - 1
            if direction == 'W': current_x = current_x + 1
            current = (current_y, current_x)
            if current in visited: return True
            visited.add(current)
        return False

        
# @lc code=end

