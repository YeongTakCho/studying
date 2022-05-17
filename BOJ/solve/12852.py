import sys
from collections import deque
sys.setrecursionlimit(10**6)

x = int(input())
d = deque()
d.append([x, 0, [x]])

visited = [False] * (x+1)
visited[x] = True

while True:
    n, c, arr = d.popleft()
    if n == 1:
        print(c)
        print(" ".join(str(e) for e in arr))
        break
    else:
        if n % 3 == 0 and not visited[n//3]:
            d.append([n//3, c+1, arr + [n//3]])
            visited[n//3] = True
        if n % 2 == 0 and not visited[n//2]:
            d.append([n//2, c+1, arr + [n//2]])
            visited[n//2] = True
        if not visited[n-1]:
            d.append([n-1, c+1, arr + [n-1]])
            visited[n-1] = True
