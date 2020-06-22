# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/ - EASY



# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?


def getRow(rowIndex: int):
    rows = [1]
    for i in range(rowIndex):
        for i in range(len(rows)-1):
            rows[i] = rows[i] + rows[i+1]
        rows.insert(0,1)
    return rows



print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
print(getRow(5))
print(getRow(7))