# WRONG code for "BOJ 2098. 외판원 순회"
# - Problem link: https://www.acmicpc.net/problem/2098
# - MY link:
import sys

read = sys.stdin.readline
MAXSIZE = sys.maxsize


def sol():
    ans = 0
    N = int(read())
    N_arr = [i for i in range(N)]
    W = [list(map(int, read().split())) for _ in range(N)]
    isVisited = [False for _ in range(N)]

    front = 0
    end = 0
    isVisited[0] = True

    while False in isVisited:
        front_min_index = min(
            N_arr, key=lambda index: W[front][index] if W[front][index] > 0 and not isVisited[index] else MAXSIZE)
        end_min_index = min(
            N_arr, key=lambda index: W[index][end] if W[index][end] > 0 and not isVisited[index] else MAXSIZE)

        front_min_val = W[front][front_min_index]
        end_min_val = W[end_min_index][end]

        if front_min_val < end_min_val:
            ans += front_min_val
            isVisited[front_min_index] = True
            front = front_min_index
        else:
            ans += end_min_val
            isVisited[end_min_index] = True
            end = end_min_index

    return ans


print(sol())
