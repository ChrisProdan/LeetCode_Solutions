class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        myStack = [height[0]]
        tallestLeft = [0]
        
        for i in range(1,n):
            tallestLeft.append(myStack[-1])
            if height[i] > myStack[-1]:
                myStack.append(height[i])
   
        myStack = [height[-1]]
        tallestRight = [0]

        for i in range(2,n+1):
            tallestRight.insert(0,myStack[-1])
            if height[-i] > myStack[-1]:
                myStack.append(height[-i])
        
        total = 0
        for i in range(n):
            waterHeight = min(tallestLeft[i],tallestRight[i])
            if waterHeight <= height[i]:
                continue
            else:
                total += waterHeight - height[i]
        
        return total