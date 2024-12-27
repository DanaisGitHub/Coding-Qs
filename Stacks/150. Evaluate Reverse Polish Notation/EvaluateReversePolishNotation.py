class Solution:
    def stackReadjustment(self, stack:[], newValue):
        stack.pop()
        stack.pop()
        stack.append(newValue)
        return stack
    
    def evalRPN(self, tokens: list[str]) -> int:
        stack:[]=[]
        tempResult = 0
        
        for char in tokens:
            if char == "+":
                tempResult = int(stack[-2])+int(stack[-1])
                stack = self.stackReadjustment(stack,tempResult)
            elif char == "-":
                tempResult = int(stack[-2])-int(stack[-1])
                stack = self.stackReadjustment(stack,tempResult)
            elif char == "*":
                tempResult = int(stack[-2])*int(stack[-1])
                stack = self.stackReadjustment(stack,tempResult)
            elif char == "/":
                tempResult = int(stack[-2])/int(stack[-1])
                stack = self.stackReadjustment(stack,tempResult)
            else:
                stack.append(char)
        return int(stack[0])
                
                
solution = Solution()
print(solution.evalRPN(["4","13","5","/","+"]))