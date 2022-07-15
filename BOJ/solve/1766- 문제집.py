# SOLVING code for "BOJ 1766. 문제집"
# - Problem link: https://www.acmicpc.net/problem/1766
# - MY link: https://www.acmicpc.net/source/46074242
# - Used algorithm: priority queue
import heapq
import sys
read = sys.stdin.readline
VOIDSET = set()


def sol():
    ans = list()  # return val
    h = list()  # heapq
    N, M = map(int, read().split())
    before_problem = [set() for _ in range(N)]
    after_problem = [set() for _ in range(N)]

    for _ in range(M):
        A, B = map(int, read().split())
        A -= 1
        B -= 1
        before_problem[B].add(A)
        after_problem[A].add(B)

    for i in range(N):
        if before_problem[i] == VOIDSET:
            heapq.heappush(h, i)

    while h:
        val = heapq.heappop(h)
        ans .append(val + 1)

        if after_problem[val] != VOIDSET:
            for problem_index in after_problem[val]:
                before_problem[problem_index].discard(val)
                if before_problem[problem_index] == VOIDSET:
                    heapq.heappush(h, problem_index)

    return ans


print(*sol())
