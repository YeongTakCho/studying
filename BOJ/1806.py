# two point algorithm, false case: 13 1 1 1 1 1 1 10 10 10

import sys
read = sys.stdin.readline


def sol(s, lst):
    l_p = 0
    r_p = len(lst)-1
    sum_val = sum(lst)

    if sum_val < s:
        return 0

    while (sum_val > s and l_p < r_p):
        if lst[l_p] > lst[r_p]:
            sum_val -= lst[r_p]
            r_p -= 1
        else:
            sum_val -= lst[l_p]
            l_p += 1

    if sum_val >= s:
        return r_p - l_p + 1
    if sum_val < s:
        return r_p - l_p + 2


print(sol(list(map(int, read().split()))[1], list(map(int, read().split()))))
