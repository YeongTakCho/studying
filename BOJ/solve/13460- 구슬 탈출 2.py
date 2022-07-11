# SOLVING code for "BOJ 13460. 구슬 탈출 2"
# - Problem link: https://www.acmicpc.net/problem/13460
# - MY link: https://www.acmicpc.net/source/45907236 (180000KB 6088ms 2815B)
# - Better code https://www.acmicpc.net/source/45861210 (32524KB 100ms 1491B)

from collections import deque
import sys
read = sys.stdin.readline

LEFT = [0, -1]
RIGHT = [0, 1]
UP = [-1, 0]
DOWN = [1, 0]


def sol():

    ans = -1

    def moves(direction, R, B):
        poss = [R, B]

        def move(direction, pos):
            y, x = pos[0], pos[1]
            if direction == LEFT:
                while (board[y][x-1] in (1, 4)):
                    if board[y][x-1] == 4:
                        return -1
                    x -= 1
            if direction == RIGHT:
                while(board[y][x+1] in (1, 4)):
                    if board[y][x+1] == 4:
                        return -1
                    x += 1
            if direction == UP:
                while(board[y-1][x] in (1, 4)):
                    if board[y-1][x] == 4:
                        return -1
                    y -= 1
            if direction == DOWN:
                while(board[y+1][x] in (1, 4)):
                    if board[y+1][x] == 4:
                        return -1
                    y += 1
            return [y, x]

        first = [R, B].index(
            max(R, B, key=lambda pos: pos[0] * direction[0] + pos[1] * direction[1]))

        poss[first] = move(direction, poss[first])
        if poss[first] != -1:
            board[poss[first][0]][poss[first][1]] = 0

        if first == 0:
            second = 1
        else:
            second = 0
        poss[second] = move(direction, poss[second])
        if poss[first] != -1:
            board[poss[first][0]][poss[first][1]] = 1
        return poss

    n, m = map(int, read().split())
    board = [[0] * m for _ in range(n)]
    val_dict = {'#': 0, '.': 1, 'R': 2, 'B': 3, 'O': 4}
    for i in range(n):
        j = 0
        for v in read().rstrip():
            board[i][j] = val_dict[v]
            j += 1

    R = list()
    B = list()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                R = [i, j]
                board[i][j] = 1
            if board[i][j] == 3:
                B = [i, j]
                board[i][j] = 1

    queue = deque([[R, B, UP, 1], [R, B, DOWN, 1], [
                  R, B, LEFT, 1], [R, B, RIGHT, 1]])
    while(queue):
        R, B, direction, n_moves = queue.popleft()
        [R, B] = moves(direction, R, B)
        if R == -1 or B == -1:
            if R == -1 and B != -1:
                ans = n_moves
                break
            continue

        if n_moves == 10:
            continue
        n_moves += 1
        queue.append([R, B, UP, n_moves])
        queue.append([R, B, DOWN, n_moves])
        queue.append([R, B, LEFT, n_moves])
        queue.append([R, B, RIGHT, n_moves])

    return ans


print(sol())
