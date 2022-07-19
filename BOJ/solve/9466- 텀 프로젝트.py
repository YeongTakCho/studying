#  Solve code for "BOJ {9466}. {팀 프로젝트}".

# - Problem link:https://www.acmicpc.net/problem/9466
# - MY link: https://www.acmicpc.net/source/46316708
# - Solution: dfs

import sys
read = sys.stdin.readline


def sol(lst):
    lst = list(map(lambda val: val-1, lst))
    n = len(lst)
    visited = [False] * n
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        team = [i]
        set_team = {i}
        while True:
            next = lst[team[-1]]
            if next in set_team:
                ans += team.index(next)
                break

            if next == lst[next] or visited[next]:
                ans += len(team)
                visited[next] = True
                break

            visited[next] = True
            team.append(next)
            set_team.add(next)
    return ans


ans = list()
for _ in range(int(read())):
    read()
    ans.append((sol(list(map(int, read().split())))))
for val in ans:
    print(val)
