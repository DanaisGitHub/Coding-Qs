# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         arrayOfHashMaps:[map] = []
#         result:[[]] = []
        
#         for x in strs:
#             tempMap = {}
#             for ch in x:
#                 tempMap[ch] = tempMap[ch]+1 if ch in tempMap else 1
#         arrayOfHashMaps += tempMap
        
        
#         for eachMap in arrayOfHashMaps:
#             headMap = arrayOfHashMaps[0]
#             for eachTail in range(1,len(arrayOfHashMaps)):
#                 if len(headMap) == len(eachTail):
#                     for ch in headMap:
#                         headKey = ch
#                         headValue = headMap[ch]
#                         if headKey in eachTail and headValue == eachTail[headKey] :
                            
                
        
        
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26# making an array of 0's 26 times
            
            for c in s: # for each char in a string
                count[ord(c)-ord("a")] += 1
                
            res[tuple(count)].append(s)
        
        return result.values()