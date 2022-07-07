import sys
read = sys.stdin.readline

data = [0] * 100
meet = [0] * 100
val = 0
n = int(read())
lines = [list(map(int, read().split())) for _ in range(n)]
lines.sort()

for i in range(n):
    data[i] = lines[i][1]
    for j in range(i):
        if data[i] < data[j]:
            meet[i] += 1
            meet[j] += 1
meets = sum(meet)
while(meets):
    maxMeetval = max(meet)
    maxindex = meet.index(maxMeetval)
    meet[maxindex] = 0
    for i in range(maxMeetval):
        if data[i] > data[maxindex]:
            meet[i] -= 1
    for i in range(maxMeetval, n):
        if data[i] < data[maxindex]:
            meet[i] -= 1

    meets -= maxMeetval*2
    val += 1
print(val)
