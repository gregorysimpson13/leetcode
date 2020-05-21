# 104. Maximum Depth of Binary Tree - EASY
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def maxDepth(root) -> int:
    def getDepth(node, depth=0):
        if node == None:
            return depth
        return max(getDepth(node.left, depth+1), getDepth(node.right, depth+1))
    return getDepth(root, 0)
        



root = TreeNode(3, TreeNode(9), TreeNode(20))
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root), 3)
print(maxDepth(None), 0)