# SOLVING code for "BOJ 9935. 문자열 폭발"
# - Problem link: https://www.acmicpc.net/problem/9935
# - MY link:
# - Used algorithm:
s = input()
separater = list(input())
len_sep = len(separater)

stack = list()
for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= len_sep:
        if stack[-len_sep:] == separater:
            for i in range(len_sep):
                stack.pop()

print("".join(stack) if stack else "FRULA")
