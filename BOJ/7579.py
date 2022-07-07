import sys
input = sys.stdin.readline
dp = [0]*10000001
can_memory
N, M = map(int, input().split())
A = list(map(int, input().split()))
m = list(map(int, input().split()))
d = list((Ad, md) for Ad, md in zip(A, m))
d.sort(key=lambda x: (-x[0], x[1]))
