# Wrong code for "BOJ 1708. 볼록 껍질".

# - Problem link: https://www.acmicpc.net/problem/1708
# - MY link: https://www.acmicpc.net/source/43505675
# - Solution link: https://wansook0316.github.io/cs/algorithm/2020/04/19/%EB%B0%B1%EC%A4%80-%EB%B3%BC%EB%A1%9D-%EA%BB%8D%EC%A7%88.html
# - Solution: Graham Scan

import sys
read = sys.stdin.readline


def get_fx(p0, p1, mul=1, only1=False):  # y= ax + b , return a, b
    if p0[0] == p1[0] and p0[1] == p1[1]:
        return False
    a = (p1[1]-p0[1]) / (p1[0]-p0[0])
    b = p0[1] - a*p0[0]
    if only1:
        return a*mul
    return [a, b]


def is_up(fx, p, mul):
    if (p[1]) * mul > (fx[0] * p[0] + fx[1]) * mul:
        return True
    return False


def ifFalse(d):
    if d == False:
        return -1e10
    return d


N = int(input())
ps = [list(map(int, input().split())) for _ in range(N)]
ans = 0

up_max = [max(ps, key=lambda p: (p[1], -p[0])),
          max(ps, key=lambda p: (p[1], p[0]))]

down_max = [max(ps, key=lambda p: (-p[1], -p[0])),
            max(ps, key=lambda p: (-p[1], p[0]))]

right_max = [max(ps, key=lambda p: (p[0], -p[1])),
             max(ps, key=lambda p: (p[0], p[1]))]

left_max = [max(ps, key=lambda p: (-p[0], -p[1])),
            max(ps, key=lambda p: (-p[0], p[1]))]

ans += len(set(list(map(tuple, up_max+down_max+left_max+right_max))))

xMax = [up_max[1], up_max[0], down_max[1], down_max[0]]
yMax = [right_max[1], left_max[1], right_max[0], left_max[0]]
cnt = 0
outside = list()

for y_direct in [1, -1]:
    for x_direct in [1, -1]:  # ru, lu, rd, ld
        xmax = xMax[cnt]
        ymax = yMax[cnt]
        cnt += 1
        fx = get_fx(xmax, ymax)
        if fx:
            for p in ps:
                if is_up(fx, p, y_direct):
                    outside.append(p)
            while outside:
                new_outside = list()

                xmax = max(outside, key=lambda p: (ifFalse(
                    get_fx(xmax, p, mul=x_direct * y_direct, only1=True)), p[0] * y_direct))

                ymax = max(outside, key=lambda p: (ifFalse(
                    get_fx(ymax, p, mul=x_direct * y_direct * -1, only1=True)), p[0] * y_direct))

                # 아마 여기서 xmax ymax가 제데로 들어가지 않아서 get_fx에서 에러가 type error가 발생
                fx = get_fx(xmax, ymax)
                if not fx:
                    ans += 1
                    break
                else:
                    ans += 2
                    for p in outside:
                        if is_up(fx, p, y_direct):
                            new_outside.append(p)
                    outside = new_outside

print(ans)
