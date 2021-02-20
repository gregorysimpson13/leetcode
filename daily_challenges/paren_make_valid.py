# Runtime: O(n); 34.4%
# Space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valids, stack = set(), []
        for i, ch in enumerate(s):
            if ch == ')' and stack: valids.update([i, stack.pop()])
            elif ch == '(': stack.append(i)
            elif ch != ')': valids.add(i)
        return "".join([s[v] for v in range(len(s)) if v in valids])
                
        