// Write a program that inserts a new number X at an index Y. For example if array = [1, 3, 5, 7] and X = 10, and Y = 2, by the end of your program array should be [1, 3, 10, 5, 7] (in other words we added '10' on index 2). Check the output of your array once your program is completed to make sure it's working correctly.

function insertXAndY(arr, X, Y) {
    var newArr = []
    for(var i=0; i<arr.length; i++) {
        if(i==Y) {
            newArr.push(X)
        }
        newArr.push(arr[i])
    }
    return newArr
}

console.log(insertXAndY([1, 3, 5, 7], 10, 2))