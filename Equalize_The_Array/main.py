#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    # freq = {}
    # for i in arr:
    #     if i in freq:
    #         freq[i] += 1
    #     else:
    #         freq[i] = 1
    # return freq

    res = []
    for i in arr:
        res.append(arr.count(i))
    if res.count(1) == len(res):
        return len(arr) - 1
    else:
        return len(res) - (max(res))
if __name__ == '__main__':    

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(str(result) + '\n')
