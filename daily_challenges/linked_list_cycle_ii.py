# Runtime: O(n^2)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return None
        slower, slow, fast = head, head, head.next
        while fast:
            while fast == slow:
                faster, start = slow, True
                while faster != slow or start:
                    start = False
                    if faster == slower: return slower
                    faster = faster.next
                slower = slower.next
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return None
