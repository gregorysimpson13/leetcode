# 11. Container with Most Water
# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

 



# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

                 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(height) -> int:
    max_area = 0
    max_num_idx = 0
    for i in range(1,len(height)):
        if height[i] > height[max_num_idx]:
            max_num_idx = i
        min_height = min(height[max_num_idx], height[i])
        max_area = max(min_height * (i - max_num_idx), max_area)
    return max_area

def maxAreaNaive(height) -> int:
    max_area = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            max_area = max((j-i) * min(height[i], height[j]), max_area)
    return max_area

def maxAreaNew(height) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        min_height = min(height[left], height[right])
        max_area = max(max_area, min_height * (right - left))
        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1
    return max_area



print('NAIVE SOLUTION')
print(maxAreaNaive([1,8,6,2,5,4,8,3,7]), 49)
print(maxAreaNaive([1,2,5,3]), 4)
print(maxAreaNaive([5,6,2,3,1,2,6,2,5,4,2,3,1]), 40)


print('\n\nDP SOLUTION')
print(maxArea([1,8,6,2,5,4,8,3,7]), 49)
print(maxArea([1,2,5,3]), 4)
print(maxArea([5,6,2,3,1,2,6,2,5,4,2,3,1]), 40)

print('\n\nNEWEST SOLUTION')
print(maxAreaNew([1,8,6,2,5,4,8,3,7]), 49)
print(maxAreaNew([1,2,5,3]), 4)
print(maxAreaNew([5,6,2,3,1,2,6,2,5,4,2,3,1]), 40)


