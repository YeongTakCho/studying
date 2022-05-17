"""TIME OVER code for "BOJ 11049. Çà·Ä °ö¼À ¼ø¼­".

- Problem link: https://www.acmicpc.net/problem/11049
- MY link: https://www.acmicpc.net/source/43454487
- Solution link: http://www.teferi.net/ps/problems/boj/11049
- Solution: (+ zip) -> time reduce
"""

INF = 1e12

N = int(input())
d = list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    d.append(list(map(int, input().split()))[1])

for distance in range(2, N+1):
    for i in range(N-distance+1):
        start = i
        end = i + distance

        dp[start][end] = INF

        for m in range(start+1, end):
            v = dp[start][m] + dp[m][end] + d[start] * d[m] * d[end]
            if v < dp[start][end]:
                dp[start][end] = v

print(dp[0][-1])
