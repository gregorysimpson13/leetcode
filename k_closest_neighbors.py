# K Closest Points to Origin
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/

# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
 

# Note:

# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

# def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
def kClosest(points, k):
    def swap(i, j, arr) -> None:
        arr[i], arr[j] = arr[j], arr[i]
    def getValue(i, arr) -> int:
        return arr[i][0] ** 2 + arr[i][1] ** 2
    def quickSelect(i, j, arr) -> int:
        wall = i
        for l in range(i, j):
            if getValue(l, arr) < getValue(j, arr):
                swap(l, wall, arr)
                wall = wall + 1
        swap(wall, j, arr)
        return wall
    left, right = 0, len(points) - 1
    while left <= right:
        p_i = quickSelect(left, right, points)
        if p_i == k:
            break
        if p_i < k:
            left = p_i + 1
        if p_i > k:
            right = p_i - 1
    return points[:k]



print(kClosest([[3,3],[5,-1],[-2,4]], 2))
print(kClosest([[1,3],[-2,2]], 1))