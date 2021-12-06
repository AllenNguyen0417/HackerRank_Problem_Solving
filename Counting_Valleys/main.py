#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    lst = []
    sea_pos = 0
    count = 0
    for i in path:
        if i == 'U':
            sea_pos += 1
        else:
            sea_pos -= 1
        lst.append(sea_pos)

    for k in range(len(lst)):
        if lst[k] < 0:
            if lst[k+1] == 0:
                count += 1

    return count
if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result) 

# a = [2,5,6,1,4,7,8]
# for i in range(len(a)):
#     print(a[i])