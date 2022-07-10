# WRONG code for "BOJ 17387. 선분 교차 2"
# - Problem link: https://www.acmicpc.net/problem/17387
# - MY link: https://www.acmicpc.net/problem/17387


import sys
read = sys.stdin.readline

x1, y1, x2, y2 = map(int, read().split())
x3, y3, x4, y4 = map(int, read().split())

a1 = (y2-y1) / (x2-x1)  # division error occur in case (0 0 0 2)
b1 = -a1 * x1 + y1

a2 = (y4-y3) / (x4-x3)
b2 = -a2 * x3 + y3

if a1 == a2:  # prevent division error occur in parallel line
    print(0)
    sys.exit()

mx = (b1-b2) / (a2-a1)

if (mx >= min(x1, x2) and mx >= min(x3, x4) and mx <= max(x3, x4) and mx <= max(x1, x2)):
    print(1)
else:
    print(0)
