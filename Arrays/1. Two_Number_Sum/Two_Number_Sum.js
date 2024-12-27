//import  {binarySearch} from "../../Famous Algos/Binary Search/BinarySearch";
const binarySearch = require("../../Famous Algos/Binary Search/BinarySearch");
console.log(binarySearch);

const twoNumberSum = (array, targetSum) => {
  const sortedArray = array.sort((a, b) => a - b); // (merge || quick) sort
  let result = [];
  const midIndex = Math.floor(sortedArray.length / 2);

  for (let i = 0; i < midIndex; i++) {
    const searchNum = targetSum - sortedArray[i];
    const theBinarySearch = binarySearch(sortedArray, searchNum);
    if (theBinarySearch[0] === true) {
      result.push([sortedArray[i], searchNum]);
    }
  }

  return result;
};

console.log(twoNumberSum([1, 2, 4, 5, 7, 6, 9, 10, 11], 11));

// 0 complexity  = n/2 * nlogn