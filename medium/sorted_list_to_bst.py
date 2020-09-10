# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.arr = list()
        while head:
            self.arr.append(head.val)
            head = head.next
        return self.bst(0, len(self.arr)-1)
    def bst(self, left, right):
        if left > right: return None
        mid = (left+right) // 2
        return TreeNode(self.arr[mid], self.bst(left, mid-1), self.bst(mid+1, right))
        