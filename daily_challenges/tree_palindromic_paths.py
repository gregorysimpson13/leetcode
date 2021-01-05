# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def palindrome(node=root, has=set()):
            if not node: return 0
            newHas = has ^ set([node.val])
            if not node.left and not node.right:
                return int(len(newHas) < 2)
            return palindrome(node.left, newHas) + palindrome(node.right, newHas)
        return palindrome()