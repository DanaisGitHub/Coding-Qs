# comeback and understand

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                two_sum = nums[left] + nums[right]
                
                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Handle duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result