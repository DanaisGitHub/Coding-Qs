class Solution:

    def isPalindrome(self, s: str) -> bool:
        pointer1:int = 0
        pointer2:int = len(s)-1
        while pointer1 != pointer2 or pointer1 > pointer2:
            if not self.isAlphaNumm(s[pointer1]) and pointer1 < pointer2:
               pointer1+=1
               continue 
            if not self.isAlphaNumm(s[pointer1]) and pointer1 < pointer2:
               pointer2-=1
               continue
            if s[pointer1].lower() != s[pointer2].lower():
                 return False
        return True
    
    
    def isAlphaNumm(self,d):
        c:int = ord(d)
        if c > 47 and c<58 or c>64 and c <91 or c > 96 and c < 123:
            return True
        return False

    
                
                
            
        
    


Solution.isPalindrome("nll","A A")