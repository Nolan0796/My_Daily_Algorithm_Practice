#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    onTimeStudents = 0
    for x in range(len(a)):
        if a[x] <= 0:
            onTimeStudents += 1
        else:
            continue
    if onTimeStudents >= k:
        return "YES"
    else:
        return "NO"
    

print(angryProfessor(k=3, a=[-2,-1,0,1,2]))