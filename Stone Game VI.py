class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        Values=[]
        aliceSum = sum(aliceValues)
        bobSum = sum(bobValues)

        for i in range(n):
            Values.append(aliceValues[i]+bobValues[i])
        
        Values, aliceValues, bobValues = zip(*sorted(zip(Values, aliceValues, bobValues)))


        pointer = n-1

        while(pointer >= 0):
            if pointer == 0:
                bobSum -= bobValues[pointer]
                pointer -= 1
            else:
                bobSum -= bobValues[pointer]
                pointer -= 1
                aliceSum -= aliceValues[pointer]
                pointer -= 1
        
        if aliceSum > bobSum:
            return 1
        elif aliceSum == bobSum:
            return 0        
        else:
            return -1

        