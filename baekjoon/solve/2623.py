from collections import deque

N, M = map(int, input().split())
g = [list() for _ in range(N+1)]
ind = [0] * (N+1)
result = list()
q = deque()

for _ in range(M):
    d = list(map(int, input().split()))
    dLen = d[0]
    for i in range(dLen-1):
        g[d[i+1]].append(d[i+2])
        ind[d[i+2]] += 1

for i in range(1, N+1):
    if ind[i] == 0:
        q.append(i)

while q:
    pd = q.popleft()
    result.append(pd)

    for nxt in g[pd]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            q.append(nxt)
if max(ind) == 0:
    print(" ".join(str(e) for e in result))
else:
    print(0)
