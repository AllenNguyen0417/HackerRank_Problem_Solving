#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def app_and_del(s, t, k):
    s_length = len(s)
    t_length = len(t)

    if s_length + t_length < k: return 'Yes'

    same = 0
    for s_l, t_l in zip(s, t):
        if s_l == t_l: same += 1
        else: break
   
    extra_s = s_length - same
    extra_t = t_length - same
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2: return 'Yes'
    return 'No'
    # checker
    # s_check = []
    # for i in s:
    #     if i not in s_check:
    #         s_check.append(i)

    # t_check = []
    # for i in t:
    #     if i not in t_check:
    #         t_check.append(i)

    # if s == t and len(s) 

    # if len(t_check) == len(s_check) < k:
    #     return 'Yes'
    
    # if len(s) < len(t):
    #     return 'No'


    # similar = ""
    # for i in range(len(t)):
    #     if s[i] == t[i]:
    #         similar += t[i]
    #     else:
    #         break
    # diff = len(s) - len(similar)
    # str = s[:-(diff)]     
    # if len(s) == len(t) and len(s) + len(t) == k - 1:
    #     return 'Yes'
    # else:
    #     if t[0:diff+1] == str:
    #         if diff + (len(t) - len(str)) == k:
    #             return 'Yes'
    #         else:
    #             return 'No'
    #     else:
    #         return 'No'

if __name__ == '__main__':
    
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result + '\n')

# s = hackerhappy 11
# t = hackerrank  10