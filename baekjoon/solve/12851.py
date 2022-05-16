me, you = map(int, input().split())
move = 0
dp = []
MAX_SIZE = 100001
visited = [0] * MAX_SIZE


if me == you:
    print(0)
    print(1)
else:
    visited[me] = 1
    dp.append(me)

    while True:
        visited_p = list()
        for d in dp:
            if d+1 <= MAX_SIZE - 1:
                if visited[d+1] == 0:
                    visited_p.append([d+1, visited[d]])
            if d-1 >= 0:
                if visited[d-1] == 0:
                    visited_p.append([d-1, visited[d]])
            if d*2 <= MAX_SIZE - 1:
                if visited[d*2] == 0:
                    visited_p.append([d*2, visited[d]])
        move += 1

        for vp, moves in visited_p:
            visited[vp] += moves

        visited_p = [visited_p[0] for visited_p in visited_p]

        dp = list(set(visited_p))

        if visited[you] > 0:
            print(move)
            print(visited[you])
            break
