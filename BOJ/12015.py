A = int(input())
Ai = list(map(int, input().split()))

data = [0]*1000000
maxDataIndex = 0
for n in Ai:
    if n > data[maxDataIndex]:
        maxDataIndex += 1
        data[maxDataIndex] = n
    else:
        for i in range(1, len(data)):
            if n <= data[i]:
                data[i] = n
                break
# print(data[1:maxDataIndex+1])
print(maxDataIndex)
