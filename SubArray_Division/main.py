#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    lst = []
    res = []
    count = 0
    for i in range(0,len(s),1):
        lst.append(s[i:i+m])
    for j in lst:
        if len(j) == m:
            res.append(sum(j))
    for k in res:
        if k == d:
            count += 1
    return count



if __name__ == '__main__':
    

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)

# a = [2,2,1,4,3]
# lst = []
# res = []
# res1= []
# for i in range(0,len(a),1):
#     lst.append(a[i:i+2])
# print(lst)

# for j in lst:
#     if len(j) == 2:
#         res1.append(sum(j))
# print(res1)
