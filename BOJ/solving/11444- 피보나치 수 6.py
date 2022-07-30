# SOLVING code for " . 피보나치 수 6"
# - Problem link: https://www.acmicpc.net/problem/11444
# - MY link:
DIV = 1000


def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a + b) % DIV
        print(a, end=' ')
    return b


print(fibo(int(input())))
