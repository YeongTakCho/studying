# SOLVING code for "BOJ 12015. 가장 긴 증가하는 부분 수열 2"
# - Problem link: https://www.acmicpc.net/problem/12015
# - MY link: https://www.acmicpc.net/source/46024399
# - Used algorithm: binary search

from bisect import bisect_left


A = int(input())
arr = list(map(int, input().split()))
LIS = [0]

for i in range(A):
    val = arr[i]

    # these to binary search

    # for i in range(len(LIS_val)-1, -1, -1):
    #     if val >= LIS_val[i]:
    #         if val != LIS_val[i]:
    #             if i == len(LIS_val) - 1:
    #                 LIS_val.append(val)
    #             else:
    #                 LIS_val[i+1] = val
    #         break

    index = bisect_left(LIS, val)
    if index != len(LIS) and LIS[index] == val:
        continue
    elif index == len(LIS):
        LIS.append(val)
    else:
        LIS[index] = val

print(len(LIS) - 1)
