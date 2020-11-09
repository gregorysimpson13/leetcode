# Runtime: O(n); beats 94.34%
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDiff = float('-inf')
        queue = [(root, root.val, root.val)]
        while queue:
            node, maxVal, minVal = queue.pop(0)
            maxDiff = max(maxDiff, maxVal - minVal)
            if node.left: queue.append((node.left, max(maxVal, node.left.val), min(minVal, node.left.val)))
            if node.right: queue.append((node.right, max(maxVal, node.right.val), min(minVal, node.right.val)))
        return maxDiff
