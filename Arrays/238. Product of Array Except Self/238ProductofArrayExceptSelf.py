class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultArray = [1] * len(nums)
        
        prefix = 1
        
        for i in range(len(nums)):
            resultArray[i] = prefix
            prefix*=nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):# why is endpoint -1 and not 0
            resultArray[i] *= postfix
            postfix*=nums[i]
            
        return resultArray
        