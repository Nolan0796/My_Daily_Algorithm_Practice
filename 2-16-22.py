#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum = 0
    for x in range(0, (len(ar)),+1):
        if type(ar[x]) != int:
            return "Values in input array must be integers."
        sum += ar[x]
    return sum

ar = [1,2,4]
ar1 = [20,23,4,54]
ar2 = [13,23,44]
ar3 = [3,23,"test"]
print(simpleArraySum(ar))
print(simpleArraySum(ar1))
print(simpleArraySum(ar2))
print(simpleArraySum(ar3))

