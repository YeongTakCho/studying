# SOLVING code for "BOJ 2357. 최솟값과 최댓값"
# - Problem link: https://www.acmicpc.net/problem/2357
# - MY link: https://www.acmicpc.net/source/46133387
# - Used algorithm: segmantation Tree
# - better code: https://www.acmicpc.net/source/45844826

import sys
read = sys.stdin.readline
MAXSIZE = sys.maxsize

ans = list()

N, M = map(int, read().split())
arr = [int(read()) for _ in range(N)]
ranges = [tuple(map(int, read().split())) for _ in range(M)]


max_segTree = [0] * (4 * N)
min_segTree = [0] * (4 * N)


def make_segTree(start, end, index, Tree, isMax):
    if start == end:
        Tree[index] = arr[start]
        return
    middel = (start+end)//2
    make_segTree(start, middel, index*2+1, Tree, isMax)
    make_segTree(middel+1, end, index*2 + 2, Tree, isMax)

    Tree[index] = max(Tree[index*2+1], Tree[index*2+2]
                      ) if isMax else min(Tree[index*2+1], Tree[index*2+2])


def get_segTree(start, end, index, left, right, segTree, isMax):
    if(left > end or right < start):
        if isMax:
            return MAXSIZE * -1
        else:
            return MAXSIZE
    if (left <= start and end <= right):
        return segTree[index]

    mid = (start + end) // 2

    if isMax:
        return max(get_segTree(start, mid, index*2 + 1, left, right, segTree, isMax), get_segTree(mid+1, end, index*2 + 2, left, right, segTree, isMax))
    else:
        return min(get_segTree(start, mid, index*2 + 1, left, right, segTree, isMax), get_segTree(mid+1, end, index*2 + 2, left, right, segTree, isMax))


make_segTree(0, N-1, 0, max_segTree, True)
make_segTree(0, N-1, 0, min_segTree, False)

for start, end in ranges:
    ans.append((get_segTree(0, N-1, 0, start-1, end-1, min_segTree, False),
               get_segTree(0, N-1, 0, start-1, end-1, max_segTree, True)))


for line in ans:
    print(*line)
