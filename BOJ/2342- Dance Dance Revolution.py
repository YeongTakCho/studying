# SOLVING code for "BOJ 2342. Dance Dance Revolution"
# - Problem link: https://www.acmicpc.net/problem/2342
# - MY link:
# - Used algorithm:
import sys
MAXSIZE = sys.maxsize

moves = list(map(int, input().split()))

before_move = 0
dp = [0] + [MAXSIZE] * 4


def get_move_val(before, after):
    if before == 0 or after == 0:
        ans = 2
    elif before == after:
        ans = 1
    elif (before - after) // 2 == 0:
        ans = 4
    else:
        ans = 3
    print(before, after, ans)
    return ans


for i in range(len(moves) - 1):
    tmp_move = moves[i]
    move_val = get_move_val(before_move, moves[i])

    dp[before_move] = min(
        *map(lambda idx: dp[idx] + get_move_val(before_move, idx), (0, 1, 2, 3, 4)))
    dp[tmp_move] = MAXSIZE
    for i in range(5):
        if i == before_move or i == tmp_move:
            continue
        dp[i] += move_val
    before_move = tmp_move
print(min(dp))
