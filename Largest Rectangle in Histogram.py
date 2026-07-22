class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        LeftSmaller = [0]
        RightSmaller = [0]

        myStack = [[heights[0],1]]

        for i in range(1,n):
            count = 0
            myStack.append([heights[i],1])
            while len(myStack) > 1 and myStack[-1][0] <= myStack[-2][0]:
                    count += myStack[-2][1]
                    myStack[-1][1] += myStack[-2][1]
                    myStack.pop(-2)
            LeftSmaller.append(count)

        heights.reverse()
        myStack = [[heights[0],1]]

        for i in range(1,n):
            count = 0
            myStack.append([heights[i],1])
            while len(myStack) > 1 and myStack[-1][0] <= myStack[-2][0]:
                    count += myStack[-2][1]
                    myStack[-1][1] += myStack[-2][1]
                    myStack.pop(-2)
            RightSmaller.append(count)
        
        RightSmaller.reverse()
        heights.reverse()
        totalMax = 0
        for i in range(n):
            curMax = (RightSmaller[i] + LeftSmaller[i] + 1) * heights[i]
            totalMax = curMax if curMax > totalMax else totalMax
        return totalMax
        



