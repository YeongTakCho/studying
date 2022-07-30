# WRONG code for "BOJ 14939. 불 끄기"
# - Problem link: https://www.acmicpc.net/problem/14939
# - MY link: https://www.acmicpc.net/source/46209617
# - Used algorithm:
import sys
read = sys.stdin.readline

mxy = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))


def sol(matrix):
    def is_inside_matrix(i, j):
        if 0 <= i < 10 and 0 <= j < 10:
            return True
        return False

    def press(b, i, j):
        for mx, my in mxy:
            ni = i + my
            nj = j + mx
            if is_inside_matrix(ni, nj) and b[ni][nj] == 1:
                b[ni][nj] = 0

    case_cnt = [101] * (1 << 10)
    for test_case in range(1 << 10):
        tmp_board = [matrix[i][:] for i in range(10)]
        press_cnt = 0

        mark = 1
        for j in range(9, -1, -1):
            if test_case & mark:
                press(tmp_board, 0, j)
                press_cnt += 1
            mark <<= 1

        for i in range(1, 10):
            for j in range(10):
                if tmp_board[i-1][j] == 1:
                    press(tmp_board, i, j)
                    press_cnt += 1
        if max(tmp_board[9]) == 0:
            case_cnt[test_case] = press_cnt
    return min(case_cnt)


def symbol_to_int(symbol):
    if symbol == "O":
        return 1
    else:
        return 0


if __name__ == "__main__":
    arr = list()
    for _ in range(10):
        arr.append(list(map(symbol_to_int, list(read()))))
    ans = sol(arr)
    print(ans)
