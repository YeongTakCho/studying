# TIMEOVER code for "BOJ 2042. 구간 합 구하기"
# - Problem link: https://www.acmicpc.net/problem/2042
# - MY link:
import sys
from math import ceil, log2
read = sys.stdin.readline


def sol():
    ans = list()

    n, m, k = map(int, read().split())
    arr = [int(input()) for _ in range(n)]
    arr_index = [0 for _ in range(n)]
    process = [list(map(int, read().split())) for _ in range(m+k)]

    segTree = [0] * (2**(ceil(log2(n))+1))

    def make_segTree(start, end, index):
        if start == end:
            segTree[index] = arr[start]
            arr_index[start] = index
            return

        middel = (start + end) // 2
        make_segTree(start, middel, index*2+1)
        make_segTree(middel+1, end, index*2 + 2)
        segTree[index] = segTree[index*2+1] + segTree[index*2+2]

    make_segTree(0, n-1, 0)

    def change_segTree(pos, val):
        index = arr_index[pos]
        diff = val - segTree[index]
        segTree[index] = val

        index = (index-1) // 2
        while(index >= 0):
            segTree[index] += diff
            index = (index-1) // 2

    def sum_segTree(start, end, index, left, right):
        if(left > end or right < start):
            return 0
        if (left <= start and end <= right):
            return segTree[index]

        mid = (start + end) // 2
        return sum_segTree(start, mid, index*2 + 1, left, right) + sum_segTree(mid+1, end, index*2 + 2, left, right)

    for case, n1, n2 in process:
        if case == 1:
            change_segTree(n1-1, n2)
        if case == 2:
            ans.append(sum_segTree(0, n-1, 0, n1-1, n2-1))

    return ans


for val in sol():
    print(val)
