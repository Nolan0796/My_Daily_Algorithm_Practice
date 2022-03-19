// Given an array X of multiple values (e.g. [-3,5,1,3,2,10]), write a program that reverses the values in the array.  Once your program is done X should be in the reversed order.  Do this without creating a temporary array.  Also, do NOT use the reverse method but find a way to reverse the values in the array.

function Reversing(X) {
    for(var i=0; i<((X.length/2)); i++) {
        [X[i], X[X.length-1-i]] = [X[X.length-1-i], X[i]]
    }
    return X
}

console.log(Reversing([-3,5,1,3,2,10]))