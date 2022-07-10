# SOLVING code for "BOJ 13171. A"
# - Problem link: https://www.acmicpc.net/problem/13171
# - MY link: https://www.acmicpc.net/source/45849981
from math import log2

DIV = 1000000007


def ab_mod(a, b, x):
    return (a % x * b % x) % x


a = int(input())
x = int(input())
ans = 1

pre_multi = [a]

cnt = 2
while(cnt <= x):
    pre_multi.append((pre_multi[len(pre_multi)-1]**2) % DIV)
    cnt *= 2

while(x > 0):
    index = int(log2(x))
    ans = ab_mod(ans, pre_multi[index], DIV)

    x -= 2**index
print(ans)
