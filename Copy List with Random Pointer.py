"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        whereRandomA = {}
        count = 0
        temp = head
        while temp != None:
            whereRandomA[temp] = count
            count += 1
            temp = temp.next
        
        whereRandomList = []
        temp = head
        while temp != None:
            if temp.random == None:
                whereRandomList.append(-1)
            else:
                whereRandomList.append(whereRandomA[temp.random])
            temp = temp.next
        
        deepCopyList = []

        newHead = Node(head.val,None,None)
        deepCopyList.append(newHead)
        newHeadHolder = newHead

        temp = head.next
        while temp != None:
            newHead.next = Node(temp.val,None,None)
            newHead = newHead.next
            deepCopyList.append(newHead)
            temp = temp.next

        for i in range(len(deepCopyList)):
            if whereRandomList[i] == -1:
                deepCopyList[i].random = None
            else:
                deepCopyList[i].random = deepCopyList[whereRandomList[i]] 
        
        return newHeadHolder

        

        

        