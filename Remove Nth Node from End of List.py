# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        myStack = []
        temp = head
        while temp != None:
            myStack.append(temp)
            temp = temp.next

        if myStack[-n] == myStack[0]:
            retval = head.next
            head.next = None
            return retval
        elif n == 1:
            myStack[-2].next = None
            return head
        else:
            myStack[-(n+1)].next = myStack[-(n-1)]
            myStack[-n].next = None
            return head
            
        
        

        