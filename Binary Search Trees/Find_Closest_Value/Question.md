Given an array of numbers and a target value, write a function or method 
'findClosestValue' that finds the closest value to the target in the array. 
If there are multiple closest values, return any of them.

function findClosestValue(arr: number[], target: number): number {
    // Your implementation here
}

Example:
arr = [1, 3, 5, 7, 9]
target = 6
console.log(findClosestValue(arr, target));  // Output: 5

Please analyze the time complexity (Big O) of your solution.

Time Complexity (Big O): The time complexity of the solution should be 
O(log n) if the array is sorted, where 'n' is the number of elements in the array.









Pseudo Solution:


Func findClosestValue (value, listOfValues)
	sPointer = 0
	ePointer = listOfValues.length - 1
	Found = false
	midPoint = -1
	
	
	While sPointer <= ePointer
		midPoint = floor((sPointer + ePointer) / 2)
		If (listOfValues[midPoint] == value)
			closestValue = listOfValues[midPoint]
			Found = true
			End Loop
		If listOfValues[midPoint] > value
			sPointer = midPoint + 1
		Else
			ePointer = midPoint - 1
	
	If (!found)
		If (midPoint == 0)
			closestValue =  listOfValues[midPoint+1]
		Else If (midPoint == listOfValues.length - 1)
			closestValue =  listOfValues[midPoint-1]
		else
			closestValue = min((value - listOfValues[midPoint-1] ), ( listOfValues[midPoint+1] - value )
			
Return closestValue