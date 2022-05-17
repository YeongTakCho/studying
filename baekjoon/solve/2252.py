# 개선 할 점 : 자료구조의 단순화 예시 코드(https://www.acmicpc.net/source/43407779)
N, M = map(int, input().split())
smaller = [list() for _ in range(N)]
bigger = [list() for _ in range(N)]
exist = [i for i in range(N)]

delete = list()
nextDelete = list()
# input data
for _ in range(M):
    a, b = map(int, input().split())
    smaller[b-1].append(a-1)
    bigger[a-1] .append(b-1)

# no small person data delete
for e in exist:
    if not smaller[e]:
        delete.append(e)

# delete deleted samll person data at exist
while exist:
    for d in delete:
        exist.remove(d)
        print(d+1)

    for d in delete:
        for b in bigger[d]:
            smaller[b].remove(d)
            if not smaller[b]:
                nextDelete.append(b)

    delete = nextDelete
    nextDelete = list()
