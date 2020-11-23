# Runtime: O(n); beats 96.2%
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def post(node=root):
            if not node: return 0, 0
            l0, l1 = post(node.left)
            r0, r1 = post(node.right)
            return l1 + r1, max(node.val + l0 + r0, l1 + r1)
        return max(post())
        
