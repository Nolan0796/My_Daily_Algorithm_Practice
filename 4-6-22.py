#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    record = []
    min = scores[0]
    minCount = 0
    max = scores[0]
    maxCount = 0
    for x in range(1, len(scores)):
        if scores[x] < min:
            minCount += 1
            min = scores[x]
        elif scores[x] > max:
            maxCount += 1
            max = scores[x]
        else:
            continue
    record.append(maxCount)
    record.append(minCount)
    return record

print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))