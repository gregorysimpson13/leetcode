# Runtime: O(n log n); beats 97.46%
# Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return
        arr = []
        while head:
            arr.append(head); head = head.next
        arr.sort(key=lambda x: x.val)
        head = arr[0]
        curr = head
        for node in arr[1:]:
            curr.next = node; curr = curr.next
        curr.next = None
        return head