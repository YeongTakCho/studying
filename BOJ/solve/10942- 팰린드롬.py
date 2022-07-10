# Solving code for "BOJ 10942. 팰린드롬"
# - Problem link: https://www.acmicpc.net/problem/10942
# - MY link: https://www.acmicpc.net/source/45825029

import sys
read = sys.stdin.readline

ans = list()


read()
lst = list(map(int, read().split()))
sections = [list(map(int, read().split())) for _ in range(int(read()))]
dp = [0] * (len(lst) * 2 - 1)

for i in range(len(lst)*2-1):
    if i % 2 == 0:
        dp[i] = 0
        e_p = i//2-1
        l_p = i//2+1
        while(e_p >= 0 and l_p < len(lst)):
            if lst[e_p] == lst[l_p]:
                dp[i] += 1
                e_p -= 1
                l_p += 1
            else:
                break
    else:
        dp[i] = -0.5
        e_p = i//2
        l_p = i//2 + 1

        while(e_p >= 0 and l_p < len(lst)):
            if lst[e_p] == lst[l_p]:
                dp[i] += 1
                e_p -= 1
                l_p += 1
            else:
                break

for section in sections:
    start = section[0] - 1
    end = section[1]-1
    if dp[start + end] >= (end-start) // 2:
        ans.append(1)
    else:
        ans.append(0)

for val in ans:
    print(val)
