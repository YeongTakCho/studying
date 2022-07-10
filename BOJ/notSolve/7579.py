min_cost = 10**10

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = dict()

for i in range(n):
    memory = memories[i]
    cost = costs[i]

    append_list = []
    for key in dp:
        if key >= m:
            continue
        if key + memory not in dp:
            append_list.append((key+memory, dp[key] + cost))
        elif dp[key+memory] > dp[key]+cost:
            dp[key+memory] = dp[key]+cost

    if memory not in dp:
        dp[memory] = cost
    elif dp[memory] > cost:
        dp[memory] = cost

    for k, v in append_list:
        dp[k] = v
for key in list(dp.keys()):
    if key >= m:
        if dp[key] < min_cost:
            min_cost = dp[key]
print(dp)
print(min_cost)
