# SOLVING code for "BOJ 9328. 열쇠"
# - Problem link: https://www.acmicpc.net/problem/9328
# - MY link:
from collections import deque
import sys
read = sys.stdin.readline

ans = list()


def sol():
    ans = 0
    key = set()
    locked_door = dict()
    q = deque()

    h, w = map(int, read().split())
    graph = [list(read().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    for key_val in read().rstrip():
        key.add(key_val)

    for i in range(w):
        if graph[0][i] != '*':
            q.append((0, i))
        if graph[h-1][i] != '*':
            q.append((h-1, i))
    for i in range(1, h-1):
        if graph[i][0] != '*':
            q.append((i, 0))
        if graph[i][w-1] != '*':
            q.append((i, w-1))

    while(q):
        h, w = q.popleft()
        if visited[h][w]:
            continue

        val = graph[h][w]

        if val.isalpha():  # key or door
            if val.isupper():  # door
                pass
            else:  # key
                pass
        else:  # way
            pass
    return ans


T = int(read())
for _ in range(T):
    ans.append(sol())

print(ans)

# for val in ans:
#     print(ans)
