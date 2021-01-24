# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        dummy = ListNode(); next_node = dummy
        while True:
            ptr, idx = None, 0
            for i, node in enumerate(lists):
                if not node: continue
                if not ptr: ptr = node; idx = i
                elif ptr and node.val < ptr.val: ptr = node; idx = i
            if ptr:
                next_node.next = ptr
                next_node = next_node.next
                lists[idx] = lists[idx].next
            else: break
        return dummy.next