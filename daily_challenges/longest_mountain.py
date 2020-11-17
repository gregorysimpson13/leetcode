# Runtime: O(n); beats 99.02%
# Space: O(1)
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        direction = curr_len = 1
        valid_len, prev = 0, A[0]
        for curr in A[1:]:
            if prev == curr: curr_len = 1; direction = 1
            elif direction and prev < curr: curr_len += 1
            elif direction and curr_len != 1 and prev > curr: curr_len += 1; direction = 0; valid_len = max(valid_len, curr_len)
            elif direction and curr_len == 1 and prev >= curr: curr_len = 1
            elif not direction and prev > curr: curr_len += 1; valid_len = max(valid_len, curr_len)
            elif not direction and prev < curr: curr_len = 2; direction = 1
            prev = curr
        return valid_len
