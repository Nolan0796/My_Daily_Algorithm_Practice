#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    spaces = n-1
    pounds = 1
    for x in range(n):
        print(spaces*" " + pounds*"#")
        spaces -= 1
        pounds += 1

staircase(0)
staircase(6)
staircase(10)