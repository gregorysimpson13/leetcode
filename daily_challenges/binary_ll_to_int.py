# Runtime: O(n); beats 80.37%
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val = 0
        while head:
            val, head = (val << 1) + head.val, head.next
        return val
