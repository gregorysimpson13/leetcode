# Runtime: O(n); beats 20.25%
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def merge_sort(i,j):
            if i > j: return []
            if i == j: return [asteroids[i]]
            mid = (i+j)//2
            left_arr, right_arr = merge_sort(i,mid), merge_sort(mid+1, j)
            l , r = len(left_arr) - 1, 0
            while l >= 0 and r < len(right_arr):
                if left_arr[l] > 0 and right_arr[r] < 0:
                    l_abs, r_abs = abs(left_arr[l]), abs(right_arr[r])
                    if l_abs == r_abs: l -= 1; r += 1
                    if l_abs > r_abs: r += 1
                    if l_abs < r_abs: l -= 1
                else: break
            return left_arr[0:l+1] + right_arr[r:]
        return merge_sort(0, len(asteroids)-1)


# Runtime: O(n); beats 55.79%
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = []
        for ast in asteroids:
            prev = None if not arr else arr.pop()
            while (ast != None and ast < 0) and (prev != None and prev > 0):
                left, right = abs(prev), abs(ast)
                if left == right: ast = None; prev = None
                if left < right: prev = None if not arr else arr.pop()
                if left > right: ast = None
            if prev != None: arr.append(prev)
            if ast != None: arr.append(ast)
        return arr
