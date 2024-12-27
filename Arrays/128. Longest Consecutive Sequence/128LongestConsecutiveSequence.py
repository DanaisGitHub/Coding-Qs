
# your version works however, small inficies cause time to run out

# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         maxSeqLength = 0
#         # convert array into set
#         setOfArray = set(nums)
        
#         for num in setOfArray:
#             tempNum = num
#             tempMax = 1
#             while (tempNum-1 in setOfArray): # 
#                 tempNum-=1
#             while (tempNum + 1 in setOfArray):
#                 tempNum+=1
#                 tempMax+=1
#             maxSeqLength = maxSeqLength if tempMax <= maxSeqLength else tempMax
            
#         return maxSeqLength
                
        
        
        
        

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxSeqLength = 0
        # convert array into set
        setOfArray = set(nums)
        
        for num in setOfArray:
            tempNum = num
            tempMax = 1
            if tempNum-1 in setOfArray: # we will eventually hit the start which ever number it is 
                continue
            while (tempNum + 1 in setOfArray):
                tempNum+=1
                tempMax+=1
            maxSeqLength = maxSeqLength if tempMax <= maxSeqLength else tempMax
            
        return maxSeqLength
                
                
                
print(Solution.longestConsecutive(None,[100,1,2,3,4,200]))    