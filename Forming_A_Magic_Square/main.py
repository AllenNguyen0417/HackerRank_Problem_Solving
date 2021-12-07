#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here.
    possibleMagicSquare = [
                            [8,1,6,3,5,7,4,9,2],
                            [6,1,8,7,5,3,2,9,4],
                            [4,9,2,3,5,7,8,1,6],
                            [2,9,4,7,5,3,6,1,8],
                            [8,3,4,1,5,9,6,7,2],
                            [4,3,8,9,5,1,2,7,6],
                            [6,7,2,1,5,9,8,3,4],
                            [2,7,6,9,5,1,4,3,8],
                        ]
    lst = []
    res = []
    for i in range(3):
        for j in range(3):
            lst.append(s[i][j])

    diff_list = []
    res = []
    for ar in possibleMagicSquare:
        for i in range(9):
            diff_list.append(abs(ar[i]-lst[i]))
    diff_list_list = [
        diff_list[0:9],
        diff_list[9:18],
        diff_list[18:27],
        diff_list[27:36],
        diff_list[36:45],
        diff_list[45:54],
        diff_list[54:63],
        diff_list[63:72],
    ]

    for i in diff_list_list:
        res.append(sum(i))
    return min(res)


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)

# a = [1,2,3]
# b = [1,2,4]
# res = []
# diff = 0
# for i in range(3):
#     if a[i] != b[i]:
#         diff += abs(a[i]-b[i])
#         res.append(diff)
# print(res)

# a = [5,3,4,1,5,8,6,4,2]
# possibleMagicSquare = [
#                         [8,1,6,3,5,7,4,9,2],
#                         [6,1,8,7,5,3,2,9,4],
#                         [4,9,2,3,5,7,8,1,6],
#                         [2,9,4,7,5,3,6,1,8],
#                         [8,3,4,1,5,9,6,7,2],
#                         [4,3,8,9,5,1,2,7,6],
#                         [6,7,2,1,5,9,8,3,4],
#                         [2,7,6,9,5,1,4,3,8],
#                     ]
# diff_list = []
# res = []
# for ar in possibleMagicSquare:
#     for i in range(9):
#         diff_list.append(abs(ar[i]-a[i]))
# diff_list_list = [
#     diff_list[0:9],
#     diff_list[9:18],
#     diff_list[18:27],
#     diff_list[27:36],
#     diff_list[36:45],
#     diff_list[45:54],
#     diff_list[54:63],
#     diff_list[63:72],
# ]

# for i in diff_list_list:
#     res.append(sum(i))
# print(min(res))

