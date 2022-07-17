# SOLVING code for "BOJ 1644. 소수의 연속합"
# - Problem link: https://www.acmicpc.net/problem/1644
# - MY link: https://www.acmicpc.net/source/46218770
# - Used algorithm: two pointer
import re


def sol():
    n = int(input())
    isPrime = [False, False] + [True] * (n-1)
    prime_arr = list()
    for i in range(2, n+1):
        if isPrime[i]:
            prime_arr.append(i)
            for j in range(2, n//i+1):
                isPrime[i*j] = False
    count = 0
    end = 0
    tmp_sum = 0
    for start in range(len(prime_arr)):
        while tmp_sum < n and end < len(prime_arr):
            tmp_sum += prime_arr[end]
            end += 1
        if tmp_sum == n:
            count += 1
        tmp_sum -= prime_arr[start]
    return count


if __name__ == "__main__":
    print(sol())
