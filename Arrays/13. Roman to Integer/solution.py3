class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        total,i = 0,0
        if (len(s) == 1):
            return romanNums[0]
        while i < len(s):
            curChar = s[i]
            nextChar = s[i+1]
            
            if romanNums[curChar] >= romanNums[nextChar]:
                total += romanNums[curChar]
                print(romanNums[curChar]) 
                i+=1
            else:
                total += (romanNums[nextChar] - romanNums[curChar]) 
                print(romanNums[nextChar] - romanNums[curChar]) 
                i+=2
                
            if i == len(s)-1:
                total += romanNums[s[i]] 
                i+=1
                break
                
        return total
    
print(Solution.romanToInt("","MDCXCV"))