# 1326. Minimum Number of Taps to Open to Water a Garden - HARD
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

# There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

# There are n + 1 taps located at points [0, 1, ..., n] in the garden.

# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

# Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

# Example 1:


# Input: n = 5, ranges = [3,4,1,1,0,0]
# Output: 1
# Explanation: The tap at point 0 can cover the interval [-3,3]
# The tap at point 1 can cover the interval [-3,5]
# The tap at point 2 can cover the interval [1,3]
# The tap at point 3 can cover the interval [2,4]
# The tap at point 4 can cover the interval [4,4]
# The tap at point 5 can cover the interval [5,5]
# Opening Only the second tap will water the whole garden [0,5]
# Example 2:

# Input: n = 3, ranges = [0,0,0,0]
# Output: -1
# Explanation: Even if you activate all the four taps you cannot water the whole garden.
# Example 3:

# Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
# Output: 3
# Example 4:

# Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
# Output: 2
# Example 5:

# Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
# Output: 1
 

# Constraints:

# 1 <= n <= 10^4
# ranges.length == n + 1
# 0 <= ranges[i] <= 100

'''
0   1   2   3   4   5   6   7   8   9   10
|---|---|---|---|---|---|---|---|---|---|

------------- [0,3] (0)
--------------------- [0,5] (1)
     -------- [1,3] (2)
            - [3,3] (3)
                - [4,4] (4)




lenght of garden is n
starts at 0
ends at n

create new list of start and end positions
sort by start position
set right to 0
select best tap:
    loop through all indexes of taps
        if we cannot make a selection return -1
        set right to selection farright
        loop through all elements that covers right
            set farright to max right
        increment taps
        if farright >= n: return taps
        set inner index to outter index
'''

def minTaps(n, ranges):
    taps_list = []
    for index in range(len(ranges)):
        start = index - ranges[index] if index - ranges[index] >= 0 else 0
        end = index + ranges[index] if index + ranges[index] <= n else n
        taps_list.append((start, end))
    taps_list.sort(key=lambda x:x[0])
    right, idx, taps = 0, 0, 0
    while idx < len(taps_list):
        if taps_list[idx][0] > right: return -1   # if the next object cannot cover right
        farRight = taps_list[idx][1]
        while idx < len(taps_list) and taps_list[idx][0] <= right:
            farRight = max(farRight, taps_list[idx][1])
            idx += 1
        taps += 1
        right = farRight
        if right >= n:
            return taps
    return -1
            
                




print(minTaps(3, [0,0,0,0]), -1)
print(minTaps(7, [1,2,1,0,2,1,0,1]), 3)
print(minTaps(8, [4,0,0,0,0,0,0,0,4]), 2)
print(minTaps(8, [4,0,0,0,4,0,0,0,4]), 1)
print(minTaps(5, [3,4,1,1,0,0]), 1)