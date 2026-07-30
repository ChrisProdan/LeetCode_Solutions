# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        singleJump = head.next
        doubleJump = head.next.next

        if doubleJump == None:
            return False

        while True:
            if singleJump == doubleJump:
                return True
            elif doubleJump.next == None or doubleJump.next.next == None:
                return False
            else:
                singleJump = singleJump.next
                doubleJump = doubleJump.next.next
        
        