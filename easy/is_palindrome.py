# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    node_list = []
    while head:
        node_list.append(head.val)
        head = head.next
    while node_list:
        if len(node_list) == 1:
            break
        if node_list.pop(0) != node_list.pop():
            return False
    return True

def is_palindrome(head: ListNode) -> bool:
    def palindrome(node):
        if node == None:
            return True
        res = palindrome(node.next)
        nonlocal head
        if head.val != node.val:
            return False
        head = head.next
        return res
    return palindrome(head)


def getHead(vals):
    head = ListNode(vals[0])
    nxt = head
    for val in vals[1:]:
        nxt.next = ListNode(val)
        nxt = nxt.next
    return head


# print(isPalindrome(getHead([1,2,2,1])))
# print(isPalindrome(getHead([1,2,4,2,1])))
print(is_palindrome(getHead([1,2,2,1])))
print(is_palindrome(getHead([1,2,4,2,1])))
print(is_palindrome(getHead([1,2,3,5,4,2,1])))
print(is_palindrome(getHead([1])))
print(is_palindrome(getHead([1,2])))
print(is_palindrome(getHead([1,1])))


