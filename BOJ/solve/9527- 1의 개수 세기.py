# SOLVE code for "BOJ 9527. 1의 개수 세기"
# - Problem link: https://www.acmicpc.net/problem/9527
# - MY link: https://www.acmicpc.net/source/46545410
# - Used algorithm: dp

from math import log2


A,  B = map(int, input().split())

double_arr = []


def make_double_arr(n):
    global double_arr
    double_arr = [1] + [0] * (n-1)
    for i in range(1, n):
        double_arr[i] = double_arr[i-1] * 2 + 2 ** i


def get1num(n):
    if n <= 0:  # 왜 < 안붙이면 오류나는건지 모르겠음
        return 0
    if n == 1:
        return 1
    intval = int(log2(n))
    if n == 2 ** intval:
        return double_arr[intval-1] + 1
    else:
        return double_arr[intval-1]+1 + get1num(n - 2**intval) + (n - 2**intval)


make_double_arr(int(log2(B)))

print(get1num(B) - get1num(A-1))
