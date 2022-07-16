# SOLVING code for "BOJ 14938. 서강그라운드"
# - Problem link: https://www.acmicpc.net/problem/14938
# - MY link: https://www.acmicpc.net/source/46158918
# - Used algorithm: prioirity queue

import heapq
import sys
read = sys.stdin.readline


def sol():
    n, m, r = map(int, read().split())
    items = list(map(int, read().split()))

    ways = [list() for _ in range(n)]
    for _ in range(r):
        a, b, l = map(int, read().split())
        a -= 1
        b -= 1
        ways[a].append((b, l))
        ways[b].append((a, l))

    max_items = 0
    for i in range(n):
        visited = [False] * n
        visited[i] = True

        val_items = items[i]
        h = list()
        for dest, length in ways[i]:
            remain_length = m - length
            if remain_length >= 0:
                heapq.heappush(h, ((m - length) * -1, dest))

        while h:
            remain_length, dest = heapq.heappop(h)
            remain_length *= -1

            if visited[dest]:
                continue

            else:
                visited[dest] = True
                val_items += items[dest]

                for dest, length in ways[dest]:
                    if visited[dest]:
                        continue
                    else:
                        n_remain_length = remain_length - length
                        if n_remain_length >= 0:
                            heapq.heappush(
                                h, (n_remain_length * -1, dest))
        if val_items > max_items:
            max_items = val_items
    return max_items


if __name__ == "__main__":
    ans = sol()
    print(ans)
