import sys

read = sys.stdin.readline
LEFT = -1
RIGHT = 1


def sol(s, lst):
    if max(lst) >= s:
        return 1

    ans = 0
    l_p = 0
    r_p = len(lst)-1

    while(l_p < r_p):
        sum_val = sum(lst[l_p:r_p+1])
        if sum_val < s:
            return ans
        _l_p = l_p
        _r_p = r_p
        before_action = 0
        while (sum_val > s):
            if lst[_l_p] >= lst[_r_p]:
                sum_val -= lst[_r_p]
                _r_p -= 1
                before_action = RIGHT
            else:
                sum_val -= lst[_l_p]
                _l_p += 1
                before_action = LEFT

        if before_action == LEFT:
            r_p = _r_p - 1

        elif before_action == RIGHT:
            l_p = _l_p + 1
        val = _r_p - _l_p+2
        if val < ans or ans == 0:
            ans = val
    return ans


print(sol(list(map(int, read().split()))[1], list(map(int, read().split()))))
