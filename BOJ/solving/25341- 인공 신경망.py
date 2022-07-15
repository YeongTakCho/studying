# TIMEOVER code for "BOJ 25341. 인공 신경망"
# - Problem link: https://www.acmicpc.net/problem/25341
# - MY link:
import sys
read = sys.stdin.readline


def sol():
    ans = list()

    N, M, Q = map(int, read().split())
    hidden_layers = [list(map(int, read().split())) for _ in range(M)]
    output_layer = list(map(int, read().split()))

    def cal_layers():
        ans = output_layer[-1]

        def cal_layer(arr):
            ans = arr[-1]
            num_input = arr[0]
            for i in range(num_input):
                ans += input_data[arr[1 + i]-1] * arr[1+i+num_input]
            return ans

        for i in range(M):
            ans += cal_layer(hidden_layers[i]) * output_layer[i]

        return ans

    for _ in range(Q):
        input_data = list(map(int, read().split()))
        ans.append(cal_layers())

    return ans


for val in sol():
    print(val)
