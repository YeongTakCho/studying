# SOLVING code for "BOJ 2447. 별 찍기 - 10"
# - Problem link: https://www.acmicpc.net/problem/2447
# - MY link: https://www.acmicpc.net/source/46016231
# - Better code: https://www.acmicpc.net/source/46000186
N = int(input())

graph = [[' '] * N for _ in range(N)]


def recursion(y, x, length):
    if length == 1:
        graph[y-1][x-1] = '*'

    else:
        n_length = length // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                recursion(y-i*n_length, x-j*n_length, n_length)


recursion(N, N, N)
for line in graph:
    print(''.join(line))
