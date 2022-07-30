import sys


def solution(N, W, dp):
    for i in range(N):
        for j in range(N):
            if not W[i][j]:
                W[i][j] = float('inf')

    for i in range(1, N):
        dp[i][0] = W[i][0]

    for k in range(1, N - 1):
        for route in range(1, size):
            if count(route, N) == k:
                for i in range(1, N):
                    if not isin(i, route):
                        dp[i][route] = get_minimum(N, W, i, route, dp)

    dp[0][size - 1] = get_minimum(N, W, 0, size - 1, dp)

    return dp[0][size - 1]


def count(route, N):
    cnt = 0
    for n in range(1, N):
        if route & (1 << n - 1) != 0:
            cnt += 1
    return cnt


def isin(i, route):
    if route & (1 << i - 1) != 0:
        return True
    else:
        return False


def get_minimum(N, W, i, route, dp):
    minimum_dist = float('inf')
    for j in range(1, N):
        if isin(j, route):
            before_route = route & ~(1 << j - 1)
            dist = W[i][j] + dp[j][before_route]
            if minimum_dist > dist:
                minimum_dist = dist
    return minimum_dist


N = int(sys.stdin.readline())
W = [list((map(int, sys.stdin.readline().split()))) for _ in range(N)]
size = 2 ** (N - 1)
dp = [[float('inf')] * size for _ in range(N)]
print(solution(N, W, dp))

for case in range(size):
    print(bin(case), end=' ')
print()
for line in dp:
    print(line)
