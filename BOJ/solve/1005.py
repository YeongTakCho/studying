import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

t = int(read())
anss = list()
for _t in range(t):
    n, k = map(int, read().split())
    times = list(map(int, read().split()))
    root = [[] for _ in range(n)]
    getMAXDocs = [-1 for _ in range(n)]

    for _ in range(k):
        start, end = map(int, read().split())
        root[end-1].append(start-1)

    @staticmethod
    def getMAX(start):
        if getMAXDocs[start] != -1:
            return getMAXDocs[start]
        t = times[start]
        if not root[start]:
            return t
        val = t + max([getMAX(r) for r in root[start]])
        getMAXDocs[start] = val
        return val
    w = int(read())
    ans = getMAX(w-1)
    anss.append(ans)

for ans in anss:
    print(ans)
