// Let's say we are given an array of unsorted numbers. We want to create a function called linearSearch that will take in two arguments: a number and an array. The function will return the position where the number is located in the array if found if it is not found it will return false. Go ahead and implement this algorithm.


function linearSearch(num, arr) {
    var indexes = []
    for(var i=0; i<arr.length; i++) {
        if(arr[i] == num) {
            indexes.push(i)
        }
    }
    if(indexes.length < 1) {
        return console.log(false)
    }
    else {
        return console.log(`${num} appears at indexes: ${indexes}.`)
    }

}


var arr = [24, 8, 23, 3];
linearSearch(8, arr);
linearSearch(-99, arr); 


