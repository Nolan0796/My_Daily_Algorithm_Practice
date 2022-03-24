// Write a function iFactorial

function iFactorial(num) {
    if(num == 0) { 
        var val = 0;
    }
    else {
        var val = 1;
    }
    for(var i=1; i<=num; i++) {
        val *= i;
    }
    return val
}

console.log(iFactorial(0))
console.log(iFactorial(1))
console.log(iFactorial(3))
console.log(iFactorial(5))

