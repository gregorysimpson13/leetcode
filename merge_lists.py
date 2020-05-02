# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ptr1, ptr2 = l1, l2
    head = ListNode()
    lnptr = head
    while ptr2 != None or ptr1 != None:
        if ptr2 == None:
            lnptr.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
        elif ptr1 == None:
            lnptr.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
        elif ptr1.val <= ptr2.val:
            lnptr.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
        elif ptr1.val > ptr2.val:
            lnptr.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
        lnptr = lnptr.next
    return head.next