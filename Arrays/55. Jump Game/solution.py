class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = len(nums) -1
        i,j = 0,0
        reachedEnd = False

        while(reachedEnd == False or i < maxIndex or i > 0):
            maxx = nums[i] 
            tempI = maxx+i
            j = tempI
            if nums[tempI] == 0:
                maxx -= 1
                if maxx == 0:
                    i -= 1
                    if i < 0: # at first index
                        break
                    continue
                continue
            
            i = tempI
            if i >=maxIndex:
                reachedEnd = True

        return reachedEnd



        