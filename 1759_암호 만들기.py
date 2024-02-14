# 암호 만들기
import sys
def backtracking(level=0, before_idx=-1, cnt_vowel=0, cnt_unvowel=0):
    if level == L:
        if 1 <= cnt_vowel and 2 <= cnt_unvowel:
            print(*temp, sep = '')
        return

    for idx, alphabet in enumerate(arr):
        if not visited[idx] and before_idx < idx:
            visited[idx] = True
            temp.append(alphabet)
            if alphabet in vowel:
                backtracking(level + 1, idx, cnt_vowel + 1, cnt_unvowel)
            else:
                backtracking(level + 1, idx, cnt_vowel, cnt_unvowel + 1)
            visited[idx] = False
            temp.pop()


L, C = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().rstrip().split()))
vowel = 'aeiou'
temp = []
visited = [False] * C
backtracking()

