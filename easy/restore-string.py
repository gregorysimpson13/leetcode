
# https://leetcode.com/problems/shuffle-string/submissions/

# Runtime: 48 ms, faster than 96.37% of Python3 online submissions for Shuffle String.
# Memory Usage: 14 MB, less than 14.80% of Python3 online submissions for Shuffle String.
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle_dict = {idx: letter for idx, letter in zip(indices, s)}
        return "".join([shuffle_dict[i] for i in range(len(shuffle_dict))])