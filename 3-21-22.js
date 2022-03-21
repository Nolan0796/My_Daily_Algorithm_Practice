// Given an array of multiple values (e.g. [0, -1, 2, -3, 4, -5, 6]), write a program that removes any negative values in that array.  Once your program is done, the array should be composed of only the non-negative numbers, in their original order.  Do this without creating a temporary array.

function removingNegatives(arr) {
    for(i=0; i<arr.length; i++) {
        if(arr[i] < 0) {
            arr.splice([i], 1)
        }
    }
    return arr
}

console.log(removingNegatives([0, -1, 2, -3, 4, -5, 6]))

