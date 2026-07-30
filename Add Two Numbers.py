# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0,None)
        newHeadHolder = newHead

        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                nextVal = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                
                l2 = l2.next
            elif l2 == None:
                nextVal = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                
                l1 = l1.next
            else:
                nextVal = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10              
                l1 = l1.next
                l2 = l2.next
            newHead.next = ListNode(nextVal,None)
            newHead = newHead.next
        
        if carry == 1:
            newHead.next = ListNode(1,None)

        
        return newHeadHolder.next


            
        