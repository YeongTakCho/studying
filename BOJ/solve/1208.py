# 점화식 An+1 = 2An + 1, An = 2^n-1
# n = 40일 경우, 경우의 수 = 2^40 -1 == 10^12
from collections import Counter

val = 0

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

h = int(len(arr)/2)
if s == 0:
    val -= 1
dp1 = [0]
dp2 = [0]

for i in range(0, h):
    append_arr = []
    for v in dp1:
        append_arr.append(v+arr[i])
    dp1 += append_arr
for i in range(h, len(arr)):
    append_arr = []
    for v in dp2:
        append_arr.append(v+arr[i])
    dp2 += append_arr


count1 = Counter(dp1)
count2 = Counter(dp2)
for key in count1:
    val += count1[key] * count2[s-key]

print(val)
