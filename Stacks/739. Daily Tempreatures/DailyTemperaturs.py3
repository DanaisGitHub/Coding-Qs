class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res:[int]=[]
        tempIndex = 0
        for num in temperatures:
            counter = 0
            res.append(0)#assuming no higher temperature
            
            for j in range(tempIndex,(len(temperatures))): #may get out of range
                
                if num >= temperatures[j]:
                    counter+=1
                else:
                    res.pop()
                    res.append(counter)
                    break
            tempIndex += 1
        return res
    
solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))