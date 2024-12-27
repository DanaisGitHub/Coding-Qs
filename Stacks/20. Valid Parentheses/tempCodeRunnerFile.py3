class Solution:
    def stackPeek(self, stack:[str]):
        return stack[(len(stack)-1)]
    
    def isClosingPair(open:str,close:str):
        if open == "(" and close == ")":
            return True
        if open == "[" and close == "]":
            return True
        if open == "{" and close == "}":
            return True
        else:
            return False
    
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return False
        stack.append(s[0])
        
        for char in range(1,(len(s)-1)):
            peek = self.stackPeek(stack)
            if self.isClosingPair(self,peek,char):
                stack.pop
            else:
                stack.append(char)
        
        if len(stack) != 0:
            return False
        return True
            

