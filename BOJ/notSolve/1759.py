vowel = 'a', 'e', 'i', 'o', 'u'
print(vowel)

L, C = map(int, input().split())
C = input().split()
C.sort()
print(C)

isVowel = [c in vowel for c in C]
print(isVowel)
recurse([], 0, 0)


def recurse(data, start, cnt_vowel):
    for i in range(L-start):
