#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(k, ar):
    # Write your code here
    lst = []
    count = 0
    for i in range(0,len(ar),1):
        for j in range(i+1,len(ar),1):
            lst.append([ar[i], ar[j]])      

    for x in range(0,len(lst),1):
        if (lst[x][0] + lst[x][1]) % k == 0:
            count += 1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(k, ar)

    print(result)