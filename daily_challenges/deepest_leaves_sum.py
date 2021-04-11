# Runtime: O(n) beats 98.09%
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def deep_sum(node:TreeNode=root, height:int=0):
            if not node: return -1, -1
            if not node.left and not node.right: return height, node.val
            lh, lv = deep_sum(node.left, height+1)
            rh, rv = deep_sum(node.right, height+1)
            if lh == rh: return lh, lv+rv
            return (lh, lv) if lh > rh else (rh, rv)
        return deep_sum()[1]
