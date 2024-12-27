import math
class Solution:
    def resultsTesting(self, piles:list[int],k) -> int:
        accResult = 0
        for x in piles:
            p:double = k / x # upper bound
            p = math.ceil(p)
            accResult += p
        return accResult
        
        
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        rightP = 1
        leftP = len(piles)
        minK = max(piles)
        while rightP <= leftP :
            k = (leftP+rightP)/2
            predictedK = self.resultsTesting(piles,k)
            if (h<predictedK):
                leftP = k-1
            else :
                rightP = k + 1
                minK = min(minK,predictedK)
                
        return minK
            
            
            
solution = Solution()
print(solution.minEatingSpeed([30,11,23,4,20],6))
        
        
        
        
        