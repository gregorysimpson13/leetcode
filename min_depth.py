# 111. Minimum Depth of Binary Tree - EASY

# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/


# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def minDepth(self, root: TreeNode) -> int:
    if root == None: return 0
    def getDepth(node, depth=1):
        if node == None:
            return float('inf')
        if node.left == None and node.right == None:
            return depth
        return min(getDepth(node.left, depth+1), getDepth(node.right, depth+1))
    return getDepth(root, 1)