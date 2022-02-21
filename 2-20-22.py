#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    i = candles[0]
    n = 0
    for x in range(len(candles)):
        if candles[x] == i:
            n += 1
        elif candles[x] > i:
            i = candles[x]
            n = 1
    return n

print(birthdayCakeCandles([3,2,1,3]))
print(birthdayCakeCandles([3,3,1,3]))
print(birthdayCakeCandles([5,5,5,5,20]))


