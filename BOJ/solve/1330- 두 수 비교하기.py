# SOLVING code for "BOJ 1330. 두 수 비교하기"
# - Problem link: https://www.acmicpc.net/problem/1330
# - MY link:
# - Used algorithm:

A, B = map(int, input().split())

if A > B:
    print('>')
elif A == B:
    print('==')
elif A < B:
    print('<')
