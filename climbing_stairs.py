# 70. Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return climbStairs(n-1) + climbStairs(n-2)


def climbStairsCache(n: int) -> int:
    cache = {0: 1}

    def climb(n: int) -> int:
        if n in cache:
            return cache[n]
        if n < 0:
            return 0
        cache[n] = climb(n-1) + climb(n-2)
        return cache[n]
    return climb(n)


print(climbStairs(2), climbStairsCache(2), 2)
print(climbStairs(3), climbStairsCache(3), 3)
print(climbStairs(1), climbStairsCache(1), 1)
print(climbStairs(4), climbStairsCache(4))
