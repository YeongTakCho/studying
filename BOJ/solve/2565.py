import sys
read = sys.stdin.readline

arr = list()
n = int(read())
dp = [1 for _ in range(n)]

lines = [list(map(int, read().split())) for _ in range(n)]
lines.sort()

for x, y in lines:
    arr.append(y)

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
