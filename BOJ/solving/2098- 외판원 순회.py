# WRONG code for "BOJ 2098. 외판원 순회"
# - Problem link: https://www.acmicpc.net/problem/2098
# - MY link:
import sys

read = sys.stdin.readline


def sol():
    ans = 0
    N = int(read())
    W = [list(map(int, read().split())) for _ in range(N)]


print(sol())
