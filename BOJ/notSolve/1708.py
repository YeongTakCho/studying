# Wrong code for "BOJ 1708. 볼록 껍질".

# - Problem link: https://www.acmicpc.net/problem/1708
# - MY link: https://www.acmicpc.net/source/43505675
# - Solution link: https://wansook0316.github.io/cs/algorithm/2020/04/19/%EB%B0%B1%EC%A4%80-%EB%B3%BC%EB%A1%9D-%EA%BB%8D%EC%A7%88.html
# - Solution: Graham Scan

import sys
from tracemalloc import start
read = sys.stdin.readline


def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * c[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])


N = int(input())
ps = [list(map(int, input().split())) for _ in range(N)]
ps.sort(key=lambda p: (-p[0], -p[1]))
ps[0] = start

ps.sort(key=ccw())
ans = 0


