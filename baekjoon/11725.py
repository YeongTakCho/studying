import sys
sys.setrecursionlimit(10**6)

N = int(input())

conn = [list() for _ in range(N)]
root = [0] * N

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    conn[n1-1].append(n2-1)
    conn[n2-1].append(n1-1)


def dfs(conn, root, start=0):
    for c in conn[start]:
        if c == root[start]:
            continue
        root[c] = start
        dfs(conn, root, start=c)


dfs(conn, root)
for r in root[1:]:
    print(r+1)
