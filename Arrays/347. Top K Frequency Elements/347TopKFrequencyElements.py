class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        quants = [[] for i in range(nums)+1]# creates i empty arrays in array
        theMap = {}
      
        for num in nums: # maps numbers and frequency in that order
            theMap[num] = 1 + theMap[num].get(num,0)
        
        for key,value in theMap.items():# .items = list[tuples(Key:value)]
            quants[value].append(key) # eg if num 3 apears 10 times, in the 10th index of array 3 will be appended [[][][][][][][][][][3]...]
        
        res = [] 
        for i in range(len(quants -1, 0 ,-1)): #forr (int i = freq.length-1 ; freq.length-1<0 ; i--){...}
            for n in quants[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
            
            
    

        
        
        

    # I don't know how to perform the bucket sort algorthim
    
nums = [2,2,2,2,2,3,33,3,3,4,4,4,4,4,5,55]
quants = [[] for i in range(len(nums)+1)]
print(quants)