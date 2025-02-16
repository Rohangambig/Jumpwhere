# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow =  fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True 
        
        return False
    

This is the solution from my leetcode account

Check out my leetcode profile

https://leetcode.com/u/Rohan_Ambig/
