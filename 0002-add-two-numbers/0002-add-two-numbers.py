# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head acts as a placeholder to easily build the list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Continue loop if there are nodes left to process or if there's a leftover carry
        while l1 or l2 or carry:
            # Get values, defaulting to 0 if we reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the digit value
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Advance the pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next