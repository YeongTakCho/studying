# TIME OVER code for "BOJ 10942. 팰린드롬"
# - Problem link: https://www.acmicpc.net/problem/10942
# - MY link: https://www.acmicpc.net/source/45821362
# - Solution link: If you can not solve the problem, you can insert Solution Link
# - Solution:

import sys
read = sys.stdin.readline


def sol(lst, s, e):
    while(s < e):
        if lst[s-1] == lst[e-1]:
            s += 1
            e -= 1
        else:
            return 0
    return 1


ans = list()

read()
lst = list(map(int, read().split()))
m = int(read())
sections = [list(map(int, read().split())) for _ in range(m)]

for sections in sections:
    ans.append(sol(lst, sections[0], sections[1]))

for val in ans:
    print(val)
