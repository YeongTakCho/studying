# TIMEOVER code for "BOJ 2098. 외판원 순회"
# - Problem link: https://www.acmicpc.net/problem/2098
# - MY link:
from re import L
import sys

MAXSIZE = sys.maxsize
read = sys.stdin.readline


def sol():
    global N, W, case_size, dp

    # 길이 없는 곳의 길이를 MAXSIZE로 최기화
    for i in range(N):
        for j in range(N):
            if not W[i][j]:
                W[i][j] = float('inf')

    for i in range(N):
        dp[i][0] = W[i][0]

    for visited_cnt in range(1, N-1):
        for case in range(1, case_size):
            if count(case, N) == visited_cnt:
                for i in range(N-1):
                    if isin(i, case):
                        dp[i][case] = get_minimum(N, W, i, case, dp)

    return get_minimum(N, W, 0, case_size-1, dp)


def count(case, N):
    cnt = 0
    for n in range(N-1):
        if case & (1 << n):
            cnt += 1
    return cnt


def isin(j, case):
    return True if case & (1 << j) else False


def get_minimum(N, W, i, route, dp):
    minimum_dist = float('inf')
    for j in range(1, N):
        if isin(j, route):
            before_route = route & ~(1 << j - 1)
            dist = W[i][j] + dp[j][before_route]
            if minimum_dist > dist:
                minimum_dist = dist
    return minimum_dist


if __name__ == '__main__':
    N = int(read())
    W = [list(map(int, read().split())) for _ in range(N)]
    case_size = 2 ** (N-1)
    dp = [[float('inf') for _ in range(case_size)] for _ in range(N)]
    print(sol())
    for line in dp:
        print(line)
