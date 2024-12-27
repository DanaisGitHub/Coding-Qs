#include <stdio.h>

int binarySearch(int* array, int sizeOfArray, int targetNum) {
    int startPointer = 0, endPointer = sizeOfArray - 1, midPointer, i = 0;
    int found = 0;

    for (i = 0; i < sizeOfArray; i++) {
        midPointer = (startPointer + endPointer) / 2;

        if (array[midPointer] == targetNum) {
            found = 1;
            break;
        } else {
            if (array[midPointer] > targetNum) {
                endPointer = midPointer - 1;
            } else {
                startPointer = midPointer + 1;
            }
        }
    }
    return found;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int targetNum = 0;
    int sizeOfArray = sizeof(arr) / sizeof(int);
    int result = binarySearch(arr, sizeOfArray, targetNum);
    printf("%d", result);
    return 0;
}
