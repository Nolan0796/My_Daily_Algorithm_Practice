// rBS takes in an array and a value to search for. If the value is found within the array then rBS will return the index where the found value is. If the value is not found within the array then rBS returns false. Make sure your solution is recursive. Does your function need to have optional additional parameters? After that first initial call, successive recursive calls to itself might need these. 

function rBS(arr, num, index=0, boolean = false) {
    if(index == arr.length +1) {
        return boolean
    }
    if(arr[index] == num) {
        return `The number ${num} appears at index ${index}.`
    }
    return rBS(arr, num, index+1)
}

var arr1 = [-90,-19,0,2,12,29,33,190,320]
console.log(rBS(arr1, 5))
console.log(rBS(arr1, 12))
console.log(rBS(arr1, 0))
console.log(rBS(arr1, 190))




