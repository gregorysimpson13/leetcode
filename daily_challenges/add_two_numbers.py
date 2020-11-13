# Runtime: O(n); 88.41%
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1 or l2:
            if l1: stack1.append(l1.val); l1 = l1.next
            if l2: stack2.append(l2.val); l2 = l2.next
        prevNode = node = None
        carry = 0
        while stack1 or stack2 or carry:
            val = carry
            val += stack1.pop() if stack1 else 0
            val += stack2.pop() if stack2 else 0
            carry, val = 1 if val > 9 else 0, val % 10
            node = ListNode(val, prevNode)
            prevNode = node
        return node
