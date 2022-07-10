#  code for "BOJ {9466}. {팀 프로젝트}".

# - Problem link:https://www.acmicpc.net/problem/9466
# - MY link:
# - Solution link: {If you not solve the problem, you can insert Solution Link}
# - Solution:

import sys
read = sys.stdin.readline


def sol(lst):
    n = len(lst)


t = int(read())
for _ in range(t):
    read()
    print(sol(list(map(int, read().split()))))
