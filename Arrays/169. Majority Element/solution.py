from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        threshold = len(nums)//2
        counter = 0
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                counter += 1
            else:
                counter = 0
            if counter >= threshold:
                return nums[i]
        return None


print(Solution.majorityElement("", [2,2,1,1,1,2,2]))
