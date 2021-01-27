# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
# Remark: This takes care of the case if we just have a cycle. Do a 4-cycle case. 
# Once we enter the if statement in detectCycle, slow is at head. 
​
# Time = O(n)
# Space = O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if fast == slow:
                return self.findCycle(head, slow)
        return None
    def findCycle(self, head, slow):
        cycle = head
        while cycle != slow:
            cycle = cycle.next
            slow = slow.next
        return cycle 
        
        
