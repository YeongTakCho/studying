# SOLVING code for "BOJ 1300. K번째 수"
# - Problem link: https://www.acmicpc.net/problem/1300
# - MY link:
# - Used algorithm:
import sys
read = sys.stdin.readline


def get_num(i):
    ans = 0
    for j in range(1, 100):
        ans += i//j
    return ans


for i in range(20):
    print(i, get_num(2**i))
