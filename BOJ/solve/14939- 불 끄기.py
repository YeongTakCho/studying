# SOLVING code for "BOJ 14939. 불 끄기"
# - Problem link: https://www.acmicpc.net/problem/14939
# - MY link:
# - Used algorithm:
import sys
read = sys.stdin.readline

mxy = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))


def sol(matrix):
    def is_inside_matrix(state):
        y = state[0]
        x = state[1]
        if 0 <= y < 10 and 0 <= x < 10:
            return True
        else:
            return False
    # make matrix containing number of near bulbs
    near_bulb = [[0]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                for my, mx in mxy:
                    ni = i + my
                    nj = j + mx
                    if is_inside_matrix((ni, nj)):
                        near_bulb[ni][nj] += 1
    # get index of having biggest number of near bulb
    max_arr = list(map(lambda line: max(zip(line, range(10))), near_bulb))
    max_val = max(zip(max_arr, range(10)))

    ans = 0
    while max_val[0][0] > 0:

        x = max_val[0][1]
        y = max_val[1]

        for my, mx in mxy:
            nx = x + mx
            ny = y + my
            # deleting bulbs
            if is_inside_matrix((ny, nx)) and matrix[ny][nx] == 1:
                matrix[ny][nx] = 0
                for my2, mx2 in mxy:
                    nnx = nx + mx2
                    nny = ny + my2
                    # reducing near bulb count
                    if is_inside_matrix((nny, nnx)) and near_bulb[nny][nnx] > 0:
                        near_bulb[nny][nnx] -= 1

        max_arr = list(map(lambda line: max(zip(line, range(10))), near_bulb))
        max_val = max(zip(max_arr, range(10)))
        ans += 1
    return ans


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
