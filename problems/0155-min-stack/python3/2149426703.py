class MinStack:

    def __init__(self):
        self.st=[]
        self.m=0

    def push(self, value: int) -> None:
        self.st.append(value)
        self.m=min(self.st)

    def pop(self) -> None:
        temp=self.st.pop()
        if temp==self.m:
            self.m=min(self.st)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()