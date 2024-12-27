import {binarySearch} from "../../Famous Algos/Binary Search/BinarySearchTS";

const twoNumberSum = (array:number[], targetSum:number): number[][] => {
  const sortedArray:number[] = array.sort((a:number, b:number) => a - b); // (merge || quick) sort
  let result:number[][] = [];
  const midIndex:number = Math.floor(sortedArray.length / 2);

  for (let i = 0; i < midIndex; i++) {
    const searchNum:number = targetSum - sortedArray[i];
    const theBinarySearch:[boolean,number] = binarySearch(sortedArray, searchNum);
    if (theBinarySearch[0] === true) {
      result.push([sortedArray[i], searchNum]);
    }
  }

  return result;
};

console.log(twoNumberSum([1, 2, 4, 5, 7, 6, 9, 10, 11], 11));

// 0 complexity  = n/2 * nlogn