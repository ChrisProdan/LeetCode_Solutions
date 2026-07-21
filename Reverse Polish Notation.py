class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        for s in tokens:
            if s == "+":
                a = myStack.pop(len(myStack)-1)
                b = myStack.pop(len(myStack)-1)
                myStack.append(a+b)
            elif s == "-":
                a = myStack.pop(len(myStack)-1)
                b = myStack.pop(len(myStack)-1)
                myStack.append(b-a)
            elif s == "/":
                a = myStack.pop(len(myStack)-1)
                b = myStack.pop(len(myStack)-1)
                myStack.append(int(b / a))
            elif s == "*":
                a = myStack.pop(len(myStack)-1)
                b = myStack.pop(len(myStack)-1)
                myStack.append(a*b)
            else:
                myStack.append(int(s))
        return myStack[0]


        