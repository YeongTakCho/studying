import sys
read = sys.stdin.readline


def sol(lst):
    n = len(lst)
    val = 0

    for i in range(n-1, -1, -1):
        val += lst[i][0] * lst[i-n+1][1]
        val -= lst[i-n+1][0] * lst[i][1]

    val /= 2
    val = abs(val)

    return val


n = int(read())
print(round(sol([list(map(int, read().split())) for _ in range(n)]), 2))
