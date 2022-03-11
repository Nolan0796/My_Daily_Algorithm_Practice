# Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].

import random


def randomArray(num, x=0, arr=[]):
    if x == num:
        return arr
    arr.append(random.randint(0,100))
    return randomArray(num, x+1, arr=arr)

print(randomArray(10))