#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # # Write your code here
    # lst = []
    # res = []
    # for i in range(len(a)):
    #     lst.append([])
    #     for j in a:
    #         if abs(a[i] - j) <= 1:
    #             # count += 1
    #             lst[i].insert(0, j)                
    # return lst
    # for j in lst:
    #     res.append(len(j))
    
    # return max(res) - 1   

    lst = []
    res = []
    for i in range(len(a)):
        lst.append([])
        for j in a:
            if a[i] + 1 == j or a[i] == j:
                # count += 1
                lst[i].insert(0, j)
    for i in range(len(a)):
        lst.append([])
        for j in a:
            if a[i] - 1 == j or a[i] == j:
                # count += 1
                lst[i+len(a)].insert(0, j)                       

    for j in lst:
        res.append(len(j))
    
    return max(res) 


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

# a = [[1,2],[3,4]]
# a[1].insert(0,5)
# print(a)