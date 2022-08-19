# SOLVING code for "BOJ 14725. 개미굴"
# - Problem link: https://www.acmicpc.net/problem/14725
# - MY link: https://www.acmicpc.net/source/47990086
# - Used algorithm: dfs

import sys
read = sys.stdin.readline


# root = [dict: key = name, value, index of tree, ... ]
root = [dict()]
N = int(read())

for i in range(N):
    line = read().rstrip().split()

    p_tree = root
    for j in range(1, int(line[0])+1):
        if line[j] not in p_tree[0]:
            p_tree[0][line[j]] = len(p_tree)
            p_tree.append([dict()])
        p_tree = p_tree[p_tree[0][line[j]]]


def read_tree(tree, level):  # dfs
    if not tree[0].keys():
        return

    for key in sorted(tree[0].keys()):
        print('--'*level + key)
        read_tree(tree[tree[0][key]], level+1)


read_tree(root, 0)
