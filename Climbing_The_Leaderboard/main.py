#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def dense_ranking(ranked):
    rank = 1
    rank_lst = []
    rank_lst.append(rank)
    for i in range(len(ranked)-1):
        if ranked[i+1] == ranked[i]:
            rank_lst.append(rank)
        else:
            rank += 1
            rank_lst.append(rank)
    return rank_lst

def climbingLeaderboard(ranked, player):
    # Write your code here
    res = []
    for i in range(len(player)):
        ranked.insert(len(ranked),player[i])
        ranked.sort(reverse=True)
        rank_lst = dense_ranking(ranked)
        res.append(rank_lst[ranked.index(player[i])])
        ranked.remove(player[i])
    return res

if __name__ == '__main__':

    # ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    # player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))


# a = [100, 100, 50, 40, 40, 20 ,10]
# b = [5, 25, 50, 120]
# rank_lst = dense_ranking(a)
# res = []
# for i in range(len(b)):
#     a.insert(len(a),b[i])
#     a.sort(reverse=True)
#     rank_lst = dense_ranking(a)
#     res.append(rank_lst[a.index(b[i])])
#     a.remove(b[i])
# print(res)

# # a = [100, 100, 50, 40, 40, 20 ,10, 5]
# # rank_lst = [1, 1, 2, 3, 3, 4, 5, 6]


