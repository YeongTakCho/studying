# TIMEOVER code for "BOJ 1655. 가운데를 말해요"
# - Problem link: https://www.acmicpc.net/problem/1655
# - MY link:
from bisect import bisect_left
import sys
read = sys.stdin.readline

n_arr = list()

N = int(read())
arr = [int(read()) for _ in range(N)]

for i in range(N):
    n_arr.insert(bisect_left(n_arr, arr[i]), arr[i])
    print(n_arr[i//2])
