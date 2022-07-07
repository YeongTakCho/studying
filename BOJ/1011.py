import sys
read = sys.stdin.readline
v_x = [False] * 2 ** 31
v_y = [False] * 2 ** 31
n = int(read())
for _ in range(n):
    x, y = map(int, read().split())
    print(x, y)
