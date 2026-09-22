class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        self.count=0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.count+=1

    def pop(self) -> int:
        if self.count==1:
            return self.q1.popleft()
        while self.count!=0:
            popped=self.q1.popleft()
            self.q2.append(popped)
            self.q1.append(popped)
            self.count-=1
        return self.q1.popleft()
        

    def top(self) -> int:
        if self.count==0:
            return None
        if self.count==1:
            return self.q1[0]
        while self.count!=1:
            popped=self.q1.popleft()
            self.q2.append(popped)
            self.q1.append(popped)
            self.count-=1
        return self.q1[0]

    def empty(self) -> bool:
        if len(self.q1)==0 and len(self.q2)==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()