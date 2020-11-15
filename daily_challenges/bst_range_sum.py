# Runtime: O(n); beats 38.09%
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.retVal = 0
        def dfs(node=root):
            if not node: return
            dfs(node.left)
            if low <= node.val <= high: self.retVal += node.val
            dfs(node.right)
        dfs()
        return self.retVal
