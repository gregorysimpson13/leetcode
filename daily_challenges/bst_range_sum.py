# Runtime: O(n); beats 41.18%
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node=root):
            if not node: return 0
            val = node.val if low <= node.val <= high else 0
            return val + dfs(node.left) + dfs(node.right)
        return dfs()
