import typing
class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        sList= s.split(' ')
        sList.reverse()
        resStr = ""
        print((sList))
        
        for i in range(len(sList),0):
            resStr += sList[i] + " "
            print(sList[i])
            print(i)
        
        
        resStr.strip()
        return resStr
    
    
print(Solution.reverseWords("","hello there"))
            