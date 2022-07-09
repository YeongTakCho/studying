# 참고한 알고리즘 : 3sum https://kdr0407.tistory.com/33
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
near = 10**9*3
ans = list()

# O(N ** 2)
for i in range(n-2):
    j = i+1
    k = n-1
    while (j < k):
        s = arr[i] + arr[j] + arr[k]
        if abs(s) < near:
            near = abs(s)
            ans = [arr[i], arr[j], arr[k]]
        if s < 0:
            j += 1
        elif s > 0:
            k -= 1
        elif s == 0:
            print(*ans)
            sys.exit()
print(*ans)
