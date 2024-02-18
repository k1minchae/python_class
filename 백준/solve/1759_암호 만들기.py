# 암호 만들기
import sys
def backtracking(s, level=0, cnt_vowel=0, cnt_unvowel=0):
    if level == L:
        if 1 <= cnt_vowel and 2 <= cnt_unvowel:
            print(*stack, sep = '')
        return
    for a in range(s, len(arr)):
        if arr[a] not in visited:
            visited.append(arr[a])
            stack.append(arr[a])
            if arr[a] in vowel:
                backtracking(a+1, level + 1, cnt_vowel + 1, cnt_unvowel)
            else:
                backtracking(a+1, level + 1, cnt_vowel, cnt_unvowel + 1)
            visited.pop()
            stack.pop()

L, C = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().rstrip().split()))
vowel = 'aeiou'
stack = []
visited = []
backtracking(0)

