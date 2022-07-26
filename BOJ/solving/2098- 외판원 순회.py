# TIMEOVER code for "BOJ 2098. 외판원 순회"
# - Problem link: https://www.acmicpc.net/problem/2098
# - MY link:
from itertools import starmap
import sys

MAXSIZE = sys.maxsize
read = sys.stdin.readline


def sol():
    N = int(read())
    W = list()
    for i in range(N):
        def zero_to_maxsize(val): return val if not val == 0 else MAXSIZE
        W.append(list(map(zero_to_maxsize, map(int, read().split()))))

    def recursion(not_visited, pos, cost, start):

        if not not_visited:
            # return [cost + W[pos][start], [pos]]
            return [cost + W[pos][start]]

        min_cost = (MAXSIZE, 0)
        for i in range(len(not_visited)):
            next_pos = not_visited[i]
            next_cost = cost + W[pos][next_pos]
            total_cost = recursion(
                not_visited[:i] + not_visited[i+1:], next_pos, next_cost, start)
            # if len(not_visited) == N-1:
            #     print(start, total_cost)
            if min_cost[0] > total_cost[0]:
                min_cost = total_cost

        return total_cost
        # return [total_cost[0], [pos] + total_cost[1]]

    min_total_cost = [MAXSIZE, 0]
    for start in range(N):
        total_cost = recursion(
            list(list(range(start)) + list(range(start+1, N))), start, 0, start)

        if min_total_cost[0] > total_cost[0]:
            min_total_cost = total_cost

    return min_total_cost[0]


print(sol())
