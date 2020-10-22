# Runtime: O(n)
# Space: O(1); not counting call stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def depth(node=root, d=1):
            if not node: return float('inf')
            if not node.left and not node.right: return d
            return min(depth(node.left, d + 1), depth(node.right, d + 1))
        return depth()
