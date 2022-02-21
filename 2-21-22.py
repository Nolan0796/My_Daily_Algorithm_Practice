#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    if len(arr) < 5 or len(arr) > 5:
        return "Input array must have 5 values."
    totalSum = 0
    min = arr[0]
    max = arr[0]
    for x in range(len(arr)):
        if arr[x] < min:
            min = arr[x]
        if arr[x] > max:
            max = arr[x]
        totalSum += arr[x]
    miniSum = totalSum - max
    maxSum = totalSum - min
    print(miniSum, maxSum)
    




miniMaxSum([1,3,5,7,9])
miniMaxSum([769082435, 210437958, 673982045, 375809214, 380564127])