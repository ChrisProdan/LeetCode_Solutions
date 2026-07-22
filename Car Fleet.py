class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sorted, speed_sorted = zip(*sorted(zip(position, speed)))

        #pos_sorted.reverse()
        #speed_sorted.reverse()

        #if p1 - p2 / s2 - s1 < target-p1 / s1

        myStack = []
        myStack.append([pos_sorted[0],speed_sorted[0]])
        for i in range(1,len(pos_sorted)):
            myStack.append([pos_sorted[i],speed_sorted[i]])
            while len(myStack) > 1 and (myStack[-2][1]) > myStack[-1][1] and (myStack[-1][0] - myStack[-2][0]) / (myStack[-2][1] - myStack[-1][1]) <= (target - myStack[-1][0]) / myStack[-1][1]:
                myStack.pop(-2)

        return len(myStack)



        