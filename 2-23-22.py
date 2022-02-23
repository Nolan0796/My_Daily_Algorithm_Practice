#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOnHouse = 0
    orangesOnHouse = 0
    for x in range(len(apples)):
        if (apples[x] + a) >= s and (apples[x] + a) <= t:
            applesOnHouse += 1
    for x in range(len(oranges)):
        if (oranges[x] + b) >= s and (oranges[x] + b) <= t:
            orangesOnHouse += 1
    print(applesOnHouse)
    print(orangesOnHouse)

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
