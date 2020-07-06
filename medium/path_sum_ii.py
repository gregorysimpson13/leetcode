# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        current_values_list = []
        def find_sum(node, node_sum):
            if node == None:
                return
            current_values_list.append(node.val)
            node_sum = node_sum + node.val
            if node.left == None and node.right == None:
                if node_sum == sum:
                    result.append(deepcopy(current_values_list))
            find_sum(node.left, node_sum)
            find_sum(node.right, node_sum)
            current_values_list.pop()
        find_sum(root, 0)
        return result