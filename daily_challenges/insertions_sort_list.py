# Runtime:  O(nlogn); beats 98.66
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy, node = ListNode(val=float('-inf'), next=head), head
        arr, node_map = [dummy.val], {dummy.val: dummy}
        while node:
            curr = node
            if node.val not in node_map: node_map[node.val] = node
            node, i = curr.next, bisect_left(arr, curr.val)
            curr.next, node_map[arr[i-1]].next =  node_map[arr[i-1]].next, curr
            insort_left(arr, curr.val)
        node_map[arr[-1]].next = None
        return dummy.next
            