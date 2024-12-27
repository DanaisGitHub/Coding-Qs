def findMinAreaRectangle (listOfPoints:list[tuple[int,int]]):
    minNum:int = float('inf')
    visited:list[tuple[int,int]] = []

    
    for x1,y1 in listOfPoints:
        for x2,y2 in listOfPoints:
            
            if (((x1,y2) in listOfPoints) & ((x2,y1) in listOfPoints) & (x1 != x2) & (y1 != y2) ):
                area = abs((x2 - x1) * (y2 - y1))
                #print(area) # we are getting some 0's here idk why
                minNum = min(minNum,area)
            else:
                continue

    
    if minNum == float('inf'):
        minNum = 0
    
    return minNum


print(findMinAreaRectangle([(1, 1), (1, 3), (3, 1), (3, 3), (2, 2), (4, 1)]))




################################# MORE OPTIMAL SOLUTION EXISTS THE ROTATING CALIPERS ALGO #########################
                
                
            
        

