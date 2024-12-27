class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            wordStore = set()
            currCounter = 0
            highestCount = 0
            
            for i in range(0,len(s)):
                wordStore = set(s[i])
                currCounter = 1
                highestCount = max(highestCount,currCounter)
                for j in range(i+1,len(s)):
                    if s[j] in wordStore:
                        break # dont continue 
                    currCounter+=1
                    highestCount = max(highestCount,currCounter)
                    wordStore.add(s[j]) 
            
            return highestCount
                    
                
                
                
print(Solution.lengthOfLongestSubstring("","bbbbb"))



class SolutionBetter:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
                
