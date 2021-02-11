# Runtime: O(n); beats 73.57%
# Space: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = []
        for s in path.split('/'):
            if s == '..' and arr: arr.pop()
            elif s and s != '.' and s != '..': arr.append(s)
        return "/" + "/".join(arr)