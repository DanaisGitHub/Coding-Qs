class Solution:
    
    def isAnagram (self,s:str,t:str)-> bool:
        if (len(s) != len(t)):
            return False

        sMap,tMap = {},{}
        
        for i in range(len(s)):#make map values
          sMap[s[i]] = 1 + sMap[s[i]] if s[i] in sMap else 1 # s[i] = char,  map[char] = map[char]+1 || 0 # if map[char] doesn't exsit yet
          tMap[t[i]] = 1 + tMap[t[i]] if t[i] in tMap else 1 
          
        for key in sMap: # using sMap as template and searching tMap
            value = sMap[key]
            tValue = tMap[key] if key in tMap else 0
            if tValue != value:
                return False
        
        return True
            
            
            