// Given an array of multiple values (e.g. [0, -1, 2, -3, 4, -5, 6]), write a program that removes any negative values in that array.  Once your program is done, the array should be composed of only the non-negative numbers, in their original order.  Do this without creating a temporary array.

function removingNegatives(arr) {
    var count = 0
    for(var e=0; e<arr.length; e++) {
        if(arr[e] < 0) {
            count += 1
        }
    }
    for(var i=0; i<arr.length; i++) {
        if(arr[i] < 0) {
            for(var y=i+1; y < arr.length; y++)
                if(arr[y] > -1) {
                    arr[i] = arr[y]
                    if(y < arr.length-1){
                        arr[y] = arr[y+1]
                    }
                    break
                }
        }
    }
    for(var x=0 ; x < count; x++) {
        arr.pop()
    }
    return arr
}

console.log(removingNegatives([0, -1, 2, -3, 4, -5, 6]))
