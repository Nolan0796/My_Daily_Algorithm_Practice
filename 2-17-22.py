#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    for x in range(len(arr)):
        if arr[x] == 0:
            zeros += 1
        elif arr[x] > 0:
            positives += 1
        else:
            negatives += 1

    print("{:.6f}".format(positives/len(arr)))
    print("{:.6f}".format(negatives/len(arr)))
    print("{:.6f}".format(zeros/len(arr)))
    

arr = [1,1,0,-1,-1]
arr1 = [2,2,3,0,0]

plusMinus(arr)
plusMinus(arr1)