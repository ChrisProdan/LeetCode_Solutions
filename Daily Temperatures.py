class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack = []
        Output = []
        for i in range(len(temperatures)):
            Output.append(0)


        for i in range(len(temperatures)):
            myStack.append([temperatures[i],i])

            while len(myStack) > 1 and myStack[-1][0] > myStack[-2][0]:
                Output[myStack[-2][1]] = myStack[-1][1] - myStack[-2][1]
                myStack.pop(-2)

        
        return Output       