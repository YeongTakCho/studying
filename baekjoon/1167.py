import heapq

nodeN = int(input())
maps = [[0] * nodeN for i in range(nodeN)]
heap = []

for i in range(nodeN):
    data = list(map(int, input().split()))
    node = data[0] - 1
    for i in range(1, len(data), 2):
        if data[i] == -1:
            break
        maps[node][data[i] - 1] = data[i+1]
        if node < data[i] - 1:
            heapq.heappush(heap, [data[i+1], node, data[i] - 1])

while heap:
    line, n1, n2 = heapq.heappop(heap)
    for i in range(nodeN):
        if i == n1 or i == n2 or maps[n2][i] == 0:
            continue
        nLine = line + maps[n2][i]
        if maps[n1][i] == 0 or (nLine < maps[n1][i]):
            maps[n1][i] = nLine
            if n1 > i:
                heapq.heappush(heap, [nLine, i, n1])
            else:
                heapq.heappush(heap, [nLine, n1, i])

print(max([max(mapline) for mapline in maps]))
