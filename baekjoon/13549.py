me, you = map(int, input().split())
dp = list()
move = 0
visited = [False] * 100001

while me <= 100000:
    dp.append(me)
    visited[me] = True
    me = me*2

if visited[you]:
    print(move)
else:
    while True:
        ndp = list()
        for d in dp:
            if d > 0:
                if not visited[d-1]:
                    visited[d-1] = True
                    ndp.append(d-1)
            if d < 100000:
                if not visited[d+1]:
                    visited[d+1] = True
                    ndp.append(d+1)
        move += 1

        dp = list()
        for nd in ndp:
            dp.append(nd)
            while nd * 2 <= 100000:
                nd *= 2

                if visited[nd]:
                    break
                dp.append(nd)
                visited[nd] = True

        if visited[you]:
            print(move)
            break
