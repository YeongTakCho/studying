from bisect import bisect_left
import sys
read = sys.stdin.readline


def sol(s, lst):
    ans = 0
    prefix = [0] * (len(lst)+1)
    for i in range(len(lst)):
        prefix[i+1] = prefix[i] + lst[i]

    for i in range(len(prefix)):
        base = prefix[i]
        idx = bisect_left(prefix, base + s)
        if idx >= len(prefix):
            continue
        val = idx - i
        if val < ans or ans == 0:
            ans = val

    return ans


print(sol(list(map(int, read().split()))[1], list(map(int, read().split()))))
