# TIMEOVER code for "BOJ 1520. 내리막 길"
# - Problem link: https://www.acmicpc.net/problem/1520
# - MY link:
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def sol():
    M, N = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(M)]
    ways = [[0]*N for _ in range(M)]

    def dfs(y, x):

        if y == M-1 and x == N-1:
            return 1

        if ways[y][x] != 0:
            return ways[y][x]

        val = graph[y][x]
        n_way = 0

        if x < N-1:
            if graph[y][x+1] < val:
                n_way += dfs(y, x+1)
        if x > 0:
            if graph[y][x-1] < val:
                n_way += dfs(y, x-1)
        if y < M-1:
            if graph[y+1][x] < val:
                n_way += dfs(y+1, x)
        if y > 0:
            if graph[y-1][x] < val:
                n_way += dfs(y-1, x)
        ways[y][x] = n_way
        return n_way

    return dfs(0, 0)


print(sol())
