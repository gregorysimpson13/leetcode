# Runtime: O(n); beats 552.13%
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head
        arr = []; curr = head
        while curr: arr.append(curr); curr = curr.next
        k = k % len(arr)
        if k == 0: return head
        dummy = ListNode()
        curr = dummy
        for i in range(len(arr)):
            idx = (len(arr) - k + i) % len(arr)
            curr.next = arr[idx]
            curr = curr.next
        curr.next = None
        return dummy.next
            