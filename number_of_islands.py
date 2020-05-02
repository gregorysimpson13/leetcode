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



# grid is a list of lists of strings
def number_of_islands(grid):
    rows, cols = len(grid), len(grid[0])
    def get_island(y, x, visited=[]):
        if y < 0 or y >= rows or x < 0 or x >= cols:
            return
        if grid[y][x] == '0' or (y,x) in visited:
            return
        visited.append((y,x))
        get_island(y-1, x, visited)
        get_island(y+1, x, visited)
        get_island(y, x-1, visited)
        get_island(y, x+1, visited)
        grid[y][x] = '0'
        return
    ans = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '1':
                get_island(y, x)
                ans += 1
    return ans

if __name__ == "__main__":
    # example one
    input1 = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0','0','0','0','0']]
    print(number_of_islands(input1) == 1)
    # example two
    input2 = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
    print(number_of_islands(input2) == 3)