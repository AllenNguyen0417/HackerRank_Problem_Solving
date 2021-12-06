#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def lcm(ar):
    lcm = 1
    for i in ar:
        lcm = lcm*i//gcd(lcm,i)
    return lcm

def my_gcd(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result 

def getTotalX(a, b):
    # Write your code here
    lst = []
    res = []
    a_lcm = lcm(a)
    b_gcd = my_gcd(b)
    for i in range(a_lcm, b[0]+1, a_lcm):
        lst.append(i)
    for j in lst:
        if b_gcd % j == 0:
            res.append(j)
    return len(res)
    


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

# a = [2,3]
# b = [7,8,9]
# lst1 = []
# res1 = []
# k = 0
# for i in range(a[-1],b[0]+1,1):
#     lst1.append(i)
# print(lst1)
# for i in lst1:
#     for k in range(5):
#         if i % 2 == 0:
#             res1.append(i)
        
# print(res1)

# k = 0
# for i in range(a[-1],b[0]+1,1):
#     while k < len(a):
#         print(a[k])
#         k+=1

# lst = [1,2,5,6,7,8]
# b = [11,13,16]
# for j in range(lst[-1],b[-1]+1,1):
#     print(j)

# a = [2,4]
# b = [16,32,96]
# a_lcm = lcm(a)

# for i in range(a_lcm, b[0]+1, a_lcm):
#     print(i)