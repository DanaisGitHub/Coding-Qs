import math

def twoNumberSum (array:list, targetSum:int ):
    array.sort()
    sortedArr = array
    midPos = math.floor(len(sortedArr)/2)
    resultArr = []
    
    for x in range(0,midPos):
        queryNum = targetSum - sortedArr[x]
        if queryNum in sortedArr:
            resultArr.append([sortedArr[x],queryNum]) 
    return resultArr


print(twoNumberSum([1, 2, 4, 5, 7, 6, 9, 10, 11], 11))