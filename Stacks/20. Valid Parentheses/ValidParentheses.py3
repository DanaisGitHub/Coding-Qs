class Solution:
    def stackPeek(stack:[])->str:
        if (stack == []):
            return 
        print(len(stack)-1)
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
        
        for i in range(1,(len(s))):
            peek = Solution.stackPeek(stack)
    
            if Solution.isClosingPair(peek,s[i]) == True:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) != 0:
            print(stack)
            return False
        return True
    
    
    
            

print(Solution.isValid("","(){}[]"))