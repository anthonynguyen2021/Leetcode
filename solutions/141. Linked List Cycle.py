# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Time = O(n)
        # Space = O(1)
        # Two Pointer Approach: If ll is empty, return False. Set slow pointer to head and fast pointer to head.next. 
        # Run a while loop checking fast != slow. Then check if fast is None or fast.next is None, return False.
        # Otherwise, advance slow by 1 and fast by 2. 
        if not head:
            return False
        slow = head
        fast = head.next
        while fast != slow:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next 
        return True
