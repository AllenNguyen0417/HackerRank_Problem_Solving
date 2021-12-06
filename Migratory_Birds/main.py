#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = collections.Counter(arr)
    freq = dict(freq)
    max = 0
    lst = []
    for i in freq.values():
        if i > max:
            max = i
    for j in freq:
        if freq[j] == max:
            lst.append(j)
    lst.sort()
    return lst[0]

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
