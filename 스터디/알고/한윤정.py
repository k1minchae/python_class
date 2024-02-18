# 2422 : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

result = []
stack = []
def icecream(i, j):
    if i == N and j == N:
        return
    if len(stack) == 2:
        result.append(stack[:])
        return
    if j == N:
        icecream(i+1, 0)
        return

    if arr[i][j] and j == i:   # 불가능 조합
        return
    stack.append(j+1)
    icecream(i, j+1)
    stack.pop()

