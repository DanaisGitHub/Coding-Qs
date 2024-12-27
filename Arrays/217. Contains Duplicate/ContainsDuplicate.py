
# For hashSets # time = O(n)

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for item in nums:
            if item in hashset:
                return True
            hashset.add(item)
        return False
    
    


# For Hash Maps
            
