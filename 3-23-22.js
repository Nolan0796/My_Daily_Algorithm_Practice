// Go ahead and implement a function iSum that behaves just like rSum but instead of using recursion to implement the solution it uses iteration.

function iSum(num) {
    var sum = 0
    for(var i=0; i<=num; i++) {
        sum += i
    }
    return sum
}
console.log(iSum(1))
console.log(iSum(4))
