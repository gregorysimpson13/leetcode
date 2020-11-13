# Runtime: O(n); 99.08%
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root: return 0
        self.tiltsum = 0
        def tilt(node=root):
            if not node.left and not node.right: return node.val
            left = 0 if not node.left else tilt(node.left)
            right = 0 if not node.right else tilt(node.right)
            self.tiltsum += abs(left - right)
            return node.val + left + right
        tilt()
        return self.tiltsum
