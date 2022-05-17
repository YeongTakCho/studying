# https: // www.acmicpc.net/source/43406306 더 나은 코드(폴로이드 알고리즘)
import heapq

n = int(input())
m = int(input())

graph = [[0] * n for i in range(n)]
heap = []

for i in range(m):
    p0, p1, c = list(map(int, input().split()))
    p0 -= 1
    p1 -= 1
    if(c < graph[p0][p1] or graph[p0][p1] == 0):
        graph[p0][p1] = c
        heapq.heappush(heap, [c, p0, p1])
print(graph)
while heap:
    c, p1, p2 = heapq.heappop(heap)

    if 0 < graph[p1][p2] < c:
        continue

    for i in range(n):
        if i == p1 or i == p2 or graph[p2][i] == 0:
            continue

        nLine = c + graph[p2][i]
        if graph[p1][i] == 0 or (nLine < graph[p1][i]):
            graph[p1][i] = nLine
            heapq.heappush(heap, [nLine, p1, i])

for line in graph:
    print(" ".join(str(e) for e in line))
