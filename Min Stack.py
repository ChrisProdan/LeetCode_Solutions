class MinStack:

    def __init__(self):
        self.list = []

        self.minlist = []
        

    def push(self, value: int) -> None:
        self.list.append(value)

        if len(self.minlist) == 0 or value <= self.minlist[len(self.minlist)-1]:
            self.minlist.append(value)

        

    def pop(self) -> None:
        x = self.list.pop(len(self.list)-1)
        if x == self.minlist[len(self.minlist)-1]:
            self.minlist.pop(len(self.minlist)-1)


        

    def top(self) -> int:
        return self.list[len(self.list)-1]
        

    def getMin(self) -> int:
        return self.minlist[len(self.minlist) - 1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()