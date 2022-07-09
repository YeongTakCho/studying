import sys
read = sys.stdin.readline
INF = float("inf")


def sol(lst):
    min_val = INF
    ans = []

    l_p = 0
    r_p = len(lst)-1

    while (l_p < r_p):
        val = lst[l_p] + lst[r_p]

        if abs(val) < min_val:
            min_val = abs(val)
            ans = [lst[l_p], lst[r_p]]

            if val == 0:
                return ans
        if val > 0:
            r_p -= 1
        else:
            l_p += 1
    return ans


read()
print(*sol(sorted(list(map(int, read().split())))))
