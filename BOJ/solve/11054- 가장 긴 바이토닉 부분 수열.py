# SOLVING code for "BOJ 11054. 가장 긴 바이토닉 부분 수열"
# - Problem link: https://www.acmicpc.net/problem/11054
# - MY link: https://www.acmicpc.net/source/46018960

N = int(input())
arr = list(map(int, input().split()))
length1 = [1] * N
length2 = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            length1[i] = max(length1[i], length1[j]+1)
        if arr[N-i-1] > arr[N-j-1]:

            length2[N-i-1] = max(length2[N-i-1], length2[N-j-1]+1)
sum_length = [length1[i] + length2[i] for i in range(N)]

print(max(sum_length) - 1)
