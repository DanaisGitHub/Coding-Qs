class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack:[] = ['(']
    
        return self.dfg(self,n,1,0,stack)
        
        
    
    def dfg(self, n:int, openC:int,closeC:int, stack:[str]):
        
        
        if n == openC == closeC:
            return stack
        if openC+1 < n:
            stack.append('(')
            dfg(n,openC+1,closeC,stack) 
        if closeC+1<= openC:
            stack.append(')')
            dfg(n,openC+1,closeC,stack) 
            
