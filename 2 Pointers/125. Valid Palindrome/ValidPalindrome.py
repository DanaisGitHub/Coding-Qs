class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1
        
        while pointer1 <= pointer2:
            if not self.isAlphaNumm(s[pointer1]) and pointer1 < pointer2:
                pointer1 += 1
            elif not self.isAlphaNumm(s[pointer2]) and pointer1 < pointer2:
                pointer2 -= 1
            elif s[pointer1].lower() != s[pointer2].lower():
                return False
            else:
                pointer1 += 1
                pointer2 -= 1
        
        return True
    
    def isAlphaNumm(self,d):
        c:int = ord(d)
        if c > 47 and c<58 or c>64 and c <91 or c > 96 and c < 123:
            return True
        return False

    
                
                
            

Solution.isPalindrome("nll","A A")