# Runtime: O(n); beats 90.20%
# Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow, fast = head, head.next
        while fast:
            if fast == slow: return True
            fast = fast.next.next if fast.next else None
            slow = slow.next
        return False