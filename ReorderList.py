# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        temp = head
        myStack = []

        while head != None:
            myStack.append(head)
            head = head.next
        
        myStack.pop(0)

        while len(myStack) > 0:
            if len(myStack) == 1:
                temp.next = myStack[0]
                temp = temp.next
                break
            
            temp.next = myStack.pop(-1)
            temp = temp.next
            temp.next = myStack.pop(0)
            temp = temp.next
        temp.next = None
        