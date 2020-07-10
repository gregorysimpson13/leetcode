# Flatten a Multilevel Doubly Linked List
# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

'''
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

Input: head = []
Output: []
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        next_node = head
        next_stack = []
        print()
        while next_node.child or next_node.next or next_stack:
            if next_node.child:
                if next_node.next: next_stack.append(next_node.next)
                next_node.next = next_node.child
                next_node.child.prev = next_node
                next_node.child = None
            elif not next_node.next:
                node = next_stack.pop()
                next_node.next = node
                node.prev = next_node
            while next_node.next and not next_node.child:
                next_node = next_node.next
        return head

