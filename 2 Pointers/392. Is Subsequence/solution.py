class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        if len(s) == 0:
            return True
        if len(t) ==0:
            return False
        while True:
            if t[t_i] == s[s_i]:
                s_i += 1
                if s_i >= len(s):
                    return True
            t_i+=1
            if t_i >= len(t):
                break

        return False
    
    def LastWord(self,s:str):
        s = s.split()
        print(s)
        return len(s[-1])
    
    

print(Solution.LastWord("","bsdafdsb ewfeqqef  "))