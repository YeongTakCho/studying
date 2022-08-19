# SOLVING code for "BOJ 1010. 다리 놓기"
# - Problem link: https://www.acmicpc.net/problem/1010
# - MY link:
# - Used algorith

from math import comb
for _ in range(int(input())):
    print(comb(*reversed(list(map(int, input().split())))))
