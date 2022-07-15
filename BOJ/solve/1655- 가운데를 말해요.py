# SOLVE code for "BOJ 1655. 가운데를 말해요"
# - Problem link: https://www.acmicpc.net/problem/1655
# - MY link: https://www.acmicpc.net/source/46023797
import heapq
import sys

read = sys.stdin.readline
UP = 1
DOWN = 0

ans = list()
min_heapq = list()
max_heapq = list()


N = int(read())
arr = [int(read()) for _ in range(N)]

ans.append(arr[0])
ans.append(min(arr[0], arr[1]))

min_heapq.append(max(arr[0], arr[1]))
max_heapq.append(min(arr[0], arr[1]) * -1)
switch = DOWN

for i in range(2, N):
    val = arr[i]
    if switch == DOWN:
        if val <= min_heapq[0]:
            heapq.heappush(max_heapq, val * -1)

        else:
            heapq.heappush(max_heapq, heapq.heappop(min_heapq) * -1)
            heapq.heappush(min_heapq, val)
        switch = UP
    else:
        if val >= max_heapq[0] * -1:
            heapq.heappush(min_heapq, val)
        else:
            heapq.heappush(min_heapq, heapq.heappop(max_heapq) * -1)
            heapq.heappush(max_heapq, val * -1)
        switch = DOWN
    ans.append(max_heapq[0] * -1)

for val in ans:
    print(val)
