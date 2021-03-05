# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        while headA or headB:
            if headA and headA not in nodes: nodes.add(headA); headA = headA.next
            elif headA in nodes: return headA
            if headB and headB not in nodes: nodes.add(headB); headB = headB.next
            elif headB in nodes: return headB
        return None