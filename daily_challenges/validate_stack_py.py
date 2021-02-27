# Runtime: O(n); 94.09%
# Space: O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for p in pushed:
            stack.append(p)
            while popped and stack and popped[0] == stack[-1]:
                popped.pop(0); stack.pop()
        return not stack