def combineArrays (arr1:list[any],arr2:list[any])->list[any]:
    combArray = []
    combArrayLength = (len(arr1)+len(arr2))-2
    arr1i = 0
    arr2i = 0
    
    for x in range(combArrayLength):
        if arr1[arr1i] > arr2[arr2i]:
            combArray.append(arr1[arr1i])
            arr1i+=1
        elif arr1[arr1i] < arr2[arr2i]:
            combArray.append(arr2[arr2i])
            arr2i+=1
        else:
            combArray.append(arr1[arr1i])
            combArray.append(arr2[arr2i])
            arr1i+=1
            arr2i+=1
        if arr1i == len(arr1)-1:
            for i in range(x,combArrayLength):
                combArray.append(arr2[i])
            break
        elif arr2i == len(arr2)-1:
            for i in range(x,combArrayLength):
                combArray.append(arr1[i])
            break
                
        print("arr1 ", arr1i)
        print("arr2 ",arr2i)
    return combArray
            
            
            
            
print(combineArrays([1,3,5],[2,4,6]))           
        
        
    


#def Median_of_Two_Sorted_Arrays ():
    