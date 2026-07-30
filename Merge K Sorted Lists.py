# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = []


        for bucket in lists:
            temp = bucket
            while temp != None:
                heapq.heappush(output, temp.val)
                temp = temp.next
        
        if len(output) == 0:
            return None
        
        outputHead = ListNode(output[0],None)
        holder = outputHead
        heapq.heappop(output)

        while len(output) > 0:
            outputHead.next = ListNode(output[0],None)
            outputHead = outputHead.next
            heapq.heappop(output)
        
        return holder
        