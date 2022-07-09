import heapq
import sys
read = sys.stdin.readline

ans = 0
h = list()

v, e = map(int, read().split())
graph = [[] for _ in range(v)]
visited = [False for _ in range(v)]

for _e in range(e):
    p1, p2, w = map(int, read().split())
    graph[p1-1].append((w, p2-1))
    graph[p2-1].append((w, p1-1))

# 시작 정점 0
visited[0] = True
for v in graph[0]:
    heapq.heappush(h, v)
while(h):
    w, e = heapq.heappop(h)
    if visited[e]:
        continue
    visited[e] = True
    ans += w

    for v in graph[e]:
        if not visited[v[1]]:
            heapq.heappush(h, v)
print(ans)
