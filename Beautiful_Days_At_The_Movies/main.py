#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for idx in range(i,j+1,1):
        if ((idx - int(str(idx)[::-1]))/k).is_integer() == True:
            count += 1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(result)

# a = 12345
# print(int(str(a)[::-1]))