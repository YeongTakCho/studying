# SOLVING code for "BOJ 1799. 비숍"
# - Problem link: https://www.acmicpc.net/problem/1799
# - MY link:
# - Used algorithm:
from distutils.command.build_scripts import first_line_re
import sys
read = sys.stdin.readline

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

n = int(read())
matrix = [list(map(int, read().split())) for _ in range(n)]


def in_range(y, x): return 0 <= y < n and 0 <= x < n


def press(b, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        while(in_range(ny, nx)):
            b[ny][nx] = (b[ny][nx] + 1) % 2
            ny += dy[i]
            nx += dx[i]


first_line_can_press = list()
for i in range(n):
    if matrix[0][i] == 1:
        first_line_can_press.append(i)

num_first_line_can_press = len(first_line_can_press)
for case in range(1 << num_first_line_can_press):
    tmp_board = [matrix[i][:] for i in range(n)]

    cnt = 0
    mask = 1

    for j in range(n-1, -1, -1):
        if case & mask:
            press(tmp_board, 0, first_line_can_press[j])
            cnt += 1
        mask << 1

    for i in range(1, n):
        for j in range(n):
            if tmp_board[i][j]:
                press(tmp_board, i, j)
                cnt += 1
