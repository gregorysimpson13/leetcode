# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next=head); node = dummy
        count = 0
        pl = cl = dummy
        pr = cr = head
        while node:
            if count <= k: pl, cl = cl, node
            else: pr, cr = cr, cr.next
            node, count = node.next, count + 1
        cr.val, cl.val = cl.val, cr.val
        return dummy.next
