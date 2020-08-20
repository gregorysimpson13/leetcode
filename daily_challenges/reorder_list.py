# Runtime O(n); beats 29%
# Space O(n); beats 93.9%
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        prev, curr, n = None, head, 0
        while curr:
            nodes.append(curr)
            curr = curr.next
        curr = ListNode()
        while nodes:
            curr.next = nodes.pop(0) if n % 2 == 0 else nodes.pop()
            curr = curr.next
            curr.next = None
            n = n + 1