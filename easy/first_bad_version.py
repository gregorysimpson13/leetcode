# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions[1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version.


def badVersion(arr):
    def isBadVersion(n):
        return arr[n-1]

    def firstBadVersion(n):
        cache = {n: True}

        def getItem(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = isBadVersion(n)
                return cache[n]
        if getItem(1):
            return 1
        left, right = 1, n
        mid = (left + right) // 2
        while True:
            mid = (left + right) // 2
            midVal = getItem(mid)
            if midVal == False:
                nextVal = getItem(mid+1)
                if nextVal == True:
                    return mid + 1
                left = mid
            else:
                right = mid

    return firstBadVersion(len(arr))


print(badVersion([True]))
print(badVersion([False, True]))
print(badVersion([False, False, True, True]))
print(badVersion([False, True, True, True]))
print(badVersion([False, False, False, True]))
