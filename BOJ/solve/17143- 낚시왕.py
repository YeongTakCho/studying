# SOLVING code for "BOJ 17143. 낚시왕"
# - Problem link: https://www.acmicpc.net/problem/17143
# - MY link: https://www.acmicpc.net/source/46671313
# - Better code :https://www.acmicpc.net/source/46310407
import sys
read = sys.stdin.readline

sharks = set()
R, C, M = map(int, read().split())

# 새로운 상어 리스트에 상어들을 이동 결과를 저장
# 다음 위치의 가장 근처의 상어의 크기를 반환 ( 가장 가까운 상어는 새로운 상어 리스트에 포함하지 않음 )


def move_sharks(next_fishing_state):
    global sharks
    global R, C

    def move_shark(r, c, s, d):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        r += directions[d-1][0] * s
        c += directions[d-1][1] * s
        # 0 <-> 1, 2 <-> 3
        def direction_switch(val): return val // 2 * 2 - val % 2 + 1

        def reflected(size, pos):
            cnt = 0
            while not (0 <= pos <= size):
                if pos < 0:
                    pos = abs(pos)
                elif pos > size:
                    pos = size * 2 - pos
                cnt += 1
            return pos, cnt % 2

        change_d = 0
        if not(0 <= r-1 < R):
            r, change_d = reflected(R-1, r-1)
            r += 1

        if not (0 <= c-1 < C):
            c, change_d = reflected(C-1, c-1)
            c += 1
        if change_d:
            d = direction_switch(d-1)
            d += 1
        return r, c, d

    new_target_shark = None

    new_sharks = set()  # (r,c,s,d,z)
    new_sharks_hash_map = dict()  # key: (r,c) value: (s,d,z)

    for each_shark in sharks:
        r, c, s, d, z = each_shark

        new_r, new_c, new_d = move_shark(r, c, s, d)
        if (new_r, new_c) not in new_sharks_hash_map:
            new_sharks.add((new_r, new_c, s, new_d, z))
            new_sharks_hash_map[(new_r, new_c)] = (s, new_d, z)

        else:
            existing_shark_data = new_sharks_hash_map[(new_r, new_c)]
            if z > existing_shark_data[2]:
                new_sharks.remove((new_r, new_c, *existing_shark_data))
                new_sharks.add((new_r, new_c, s, new_d, z))
                new_sharks_hash_map[(new_r, new_c)] = (s, new_d, z)

    sharks = new_sharks
    if sharks:
        new_target_shark = min(
            sharks, key=lambda shark: shark[0] if shark[1] == next_fishing_state else 101)
        if new_target_shark[1] == next_fishing_state:
            sharks.remove(new_target_shark)
            return new_target_shark[4]

    return 0


for i in range(M):
    sharks.add(tuple(map(int, read().split())))

total_shark_size = 0

# 1열의 땅과 가장 가까운 상어를 찾음
# 그 상어의 크기를 총 상어의 크기에 더하고, 상어 리스트에서 제거
if sharks:
    first_target_fish = min(sharks, key=lambda val: (val[1], val[0]))
    if first_target_fish[1] == 1:
        total_shark_size += first_target_fish[4]
        sharks.remove(first_target_fish)


for fishing_state in range(2, C+1):
    # 상어를 이동 후, 가장 가까운 상어를 찾고, 그 상어의 크기를 더함
    total_shark_size += move_sharks(fishing_state)

print(total_shark_size)
