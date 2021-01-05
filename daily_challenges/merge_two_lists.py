# Runtime: O(n); beats 91.67%
# Space: O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(); node = dummy
        while l1 and l2:
            if l1.val < l2.val: node.next, l1 = l1, l1.next
            else: node.next, l2 = l2, l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return dummy.next