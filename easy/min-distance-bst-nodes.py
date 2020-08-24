# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime: 32 ms, faster than 77.57% of Python3 online submissions for Minimum Distance Between BST Nodes.
# Memory Usage: 13.8 MB, less than 68.60% of Python3 online submissions for Minimum Distance Between BST Nodes.
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root: return None
        vals = []
        def get_vals(node):
            if not node: return
            vals.append(node.val)
            get_vals(node.right); get_vals(node.left)
        get_vals(root)
        vals.sort()
        return min([abs(num1 - num2) for num1, num2 in zip(vals[1:], vals[:-1])])