# 200. Number of Islands: MEDIUM
# https://leetcode.com/problems/number-of-islands/

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        result = 0
        def bfs(row, col):
            queue = [(row, col)]
            visited = set()
            while queue:
                r, c = queue.pop(0)
                if (r,c) in visited or r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                if grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                for next_r,next_c in [(0,1), (0,-1), (1,0), (-1,0)]:
                    queue.append((r+next_r, c+next_c))
                visited.add((r,c))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    result = result + 1
        return result

if __name__ == "__main__":
    # example one
    input1 = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0','0','0','0','0']]
    print(Solution().numIslands(input1) == 1)
    # example two
    input2 = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    print(Solution().numIslands(input2) == 3)