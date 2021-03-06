# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Example 1:
# Input: 
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation: 
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
# Example 2:
# Input: 
# asteroids = [8, -8]
# Output: []
# Explanation: 
# The 8 and -8 collide exploding each other.
# Example 3:
# Input: 
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation: 
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
# Example 4:
# Input: 
# asteroids = [-2, -1, 1, 2]
# Output: [-2, -1, 1, 2]
# Explanation: 
# The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet each other.
# Note:

# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000].

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) <= 1: return asteroids
        def collision(left, right):
            if left > right:
                return []
            if left == right:
                return [asteroids[left]]
            mid = (left + right) // 2
            left_arr, right_arr = collision(left, mid), collision(mid+1, right)
            new_arr = []
            left_ptr, right_ptr = len(left_arr) - 1, 0
            while (left_ptr >= 0 and right_ptr < len(right_arr)) and (left_arr[left_ptr] > 0 and right_arr[right_ptr] < 0):
                if abs(left_arr[left_ptr]) == abs(right_arr[right_ptr]):
                    left_ptr, right_ptr = left_ptr - 1, right_ptr + 1
                elif abs(left_arr[left_ptr]) > abs(right_arr[right_ptr]):
                    right_ptr = right_ptr + 1
                else:
                    left_ptr = left_ptr - 1
            # if we have any left over
            if left_ptr >= 0:
                new_arr = left_arr[:left_ptr+1] + new_arr
            if right_ptr < len(right_arr):
                new_arr += right_arr[right_ptr:]
            return new_arr
        return collision(0, len(asteroids) - 1)


print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
print(Solution().asteroidCollision([2, -3, -1, 1, 2, -1]))
print(Solution().asteroidCollision([5, 2, -3, -1, 1, 2, -2]))