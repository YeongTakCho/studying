# TIMEOVER code for "BOJ 1520. 내리막 길"
# - Problem link: https://www.acmicpc.net/problem/1520
# - MY link: https://www.acmicpc.net/source/46021490
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def sol():
    M, N = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(M)]
    ways = [[0]*N for _ in range(M)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(y, x):

        if y == M-1 and x == N-1:
            return 1

        if ways[y][x] != 0:
            if ways[y][x] == -1:
                return 0
            else:
                return ways[y][x]

        val = graph[y][x]
        n_way = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] < val:
                n_way += dfs(ny, nx)

        if n_way == 0:
            ways[y][x] = -1
        else:
            ways[y][x] = n_way
        return n_way

    return dfs(0, 0)


print(sol())
