# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(s + t)
    # Time: O(s + t) where s, t are length of linkedlist l1, l2, respectively.
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next 
        else:
            head = l2
            l2 = l2.next
        head.next = self.mergeTwoLists(l1, l2)
        return head
            
