# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val <= list2.val:
            temp = list1
            holder = list1
            list1 = list1.next
        else:
            temp = list2
            holder = list2
            list2 = list2.next

        while list1 != None or list2 != None:
            if list1 == None:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
            elif list2 == None:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            elif list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                
        return holder
        

        