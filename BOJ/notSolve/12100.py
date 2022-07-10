from audioop import reverse
import sys
from turtle import isdown
read = sys.stdin.readline

t = 5

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]


def move(_board, isUp, isReversed):
    arr = list(range(n))
    if isReversed:
        arr_reversed = reverse(arr)
    for p1 in arr_reversed[1:n]:
        for p2 in arr:
            if isUp:
                a = p1
                b = p2
            else:
                a = p2
                b = p1
            _board[a][b] = 0


def recurse(_board, leftTimes):
    if leftTimes == 0:
        return max(map(max, _board))
    mv = 0
    for isUp in (True, False):
        for isReversed in (True, False):
            newboard = move(_board, isUp, isReversed)
            v = recurse(newboard, leftTimes-1)
            if v > mv:
                mv = v
        return mv


print(recurse(board, 5))
