# 새로운 하노이 탑
import sys
from collections import deque
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(3)]   # 막대 A, B, C

# 옮겨야할 원판만 추려서 다시 리스트 만듦 (A:0, B:1, C:2)
lst = [[], [], []]
for i in range(3):
    # 원판이 있다면
    if arr[i][-1]:
        is_move = False
        for j in range(2, 2 + int(arr[i][0])):
            if ord(arr[i][j]) - ord('A') != i:
                is_move = True
            if is_move: lst[i].append(ord(arr[i][j])-ord('A'))

cnt = 0

def move(x):
    global cnt
    if not lst[x]:
        cnt += 1
        print(lst)
    else:
        return False

def BFS():
    q = deque()
    for i in range(3):
        if lst[i]:
            x = lst[i].pop()
            q.append([x, i])
            break

    while q:    # i는 원반 x 가 원래 들어있던 위치
        x, i = q.popleft()
        if not move(x):  # 만약 원반 x를 바로 옮길수 없다면
            for xi in range(3):
                if xi != i and (not lst[xi] or lst[xi][0] != xi):
                    lst[xi].append(x)
                    break
        for ni in range(3):
            if ni!= xi and lst[ni]:
                nx = lst[ni].pop()
                q.append([nx, ni])

BFS()
print(cnt)
