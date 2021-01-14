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
        # We move the fast pointer by one before initializing the while loop. Even though the later steps of fast is advanced by two, here just advancing by 1 is fine.
        # The while loop breaks mean that there's a cycle. If we return within the loop, we don't have a cycle. 
        slow = head
        fast = head.next
        while fast != slow:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next 
        return True
