
export const binarySearch = (sortedArray,searchTerm)=> {
    let midPointer;
    let startPointer = 0;
    let endPointer = sortedArray.length-1;
    let counter = 1;
    let found = false;
    do{
        midPointer = Math.floor((startPointer + endPointer)/2)
        if (sortedArray[midPointer] === searchTerm){
            found = true;
            break;
        }
        else{
            if (searchTerm<sortedArray[midPointer]){
                endPointer = midPointer - 1
            }
            else{
                startPointer = midPointer + 1
            }
        }
        counter++;
    }while(startPointer<=endPointer)
    
    return [found,counter];
}
