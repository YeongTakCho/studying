import sys
import heapq
import bisect
read = sys.stdin.readline

n, k = map(int, read().split())
jams = list()
bags = list()
val = 0
for i in range(n):
    w, v = map(int, read().split())
    heapq.heappush(jams, (-v, w))

bags = [int(read()) * -1 for _ in range(k)]
bags.sort()

while jams and bags:
    v, w = heapq.heappop(jams)
    idx = bisect.bisect_right(bags, w * -1)
    if idx == 0:
        continue
    bags.pop(idx-1)
    val -= v
print(val)
