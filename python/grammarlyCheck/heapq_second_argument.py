# check is second argument of heapq affect sorting heapq
import heapq

h = [[0, 1], [0, 2], [0, 3], [0, -1], [0, -5]]
heapq.heapify(h)
while h:
    print(heapq.heappop(h))

# output :[0, -5] [0, -1] [0, 1] [0, 2] [0, 3]
# result: recond argument affect heapq sorting
