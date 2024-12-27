import math

def binarySearch(array: [int],targetNum: int):
    startPointer = 0
    endPointer = len(array) -1
    found = False
    counter = 0
    
    while startPointer <= endPointer:
        counter+=1
        midPointer = math.floor((startPointer + endPointer)/2)
        
        if array[midPointer] == targetNum:
            found = True
            break
        else:
            if array[midPointer] > targetNum:
                endPointer = midPointer - 1
            else:
                startPointer = midPointer + 1
        
    return (found,counter)

print(binarySearch([1,2,3,4,5,6,7,8],0))




# O(log n)
        
