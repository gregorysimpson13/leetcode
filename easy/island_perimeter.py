# 463. Island Perimeter - EASY

# https://leetcode.com/problems/island-perimeter/
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

def islandPerimeter(grid) -> int:
    rows, cols = len(grid), len(grid[0])
    def getPerimeter(y, x, visited=set()) -> int:
        if (y,x) in visited:
            return 0
        if y >= rows or y < 0 or x >= cols or x < 0:
            return 1
        print(rows, y, cols, x)
        if grid[y][x] == 0:
            return 1
        visited.add((y,x))
        result = getPerimeter(y+1, x, visited)
        result += getPerimeter(y-1, x, visited)
        result += getPerimeter(y, x-1, visited)
        result += getPerimeter(y, x+1, visited)
        return result     
    def findCell():
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    return y, x
        return -1, -1
    starty, startx = findCell()
    if starty == -1:
        return 0
    return getPerimeter(starty,startx)



# input1 = [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# print(islandPerimeter(input1))
# input2 = [[1,1,1,1],
#  [1,1,1,1],
#  [1,1,1,1],
#  [1,1,1,1]]
# print(islandPerimeter(input2))
# input3 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0]]
# print(islandPerimeter(input3))
# input4 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,1,0,0],
#  [0,0,0,0]]
# print(islandPerimeter(input4))
# input5 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,1,1,0],
#  [0,0,0,0]]
# print(islandPerimeter(input5))
input6 = [[1,0]]
print(islandPerimeter(input6))