class MinStack:
    
    def __init__(self):
        self.stack:[]=[]
        self.minDict = {}
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minDict[len(self.stack)-1] > val:
            self.minDict[len(self.stack)] = val
        else:
            self.minDict[len(self.stack)] = minDict[len(self.stack)-1]
        
        

    def pop(self) -> None:
        if self.stack == []:
            return
        print(self.stack)
        print(self.getMin)
        self.minDict.pop(len(self.stack))
        self.stack.pop()
        
        

    def top(self) -> int:
        if self.stack == []:
            return 
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack == []:
            return 
        return self.minDict[len(self.stack)]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.pop())
print(obj.top())
print(obj.getMin())