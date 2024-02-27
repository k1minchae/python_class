# 2422 : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

cnt  = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if not arr[i][j] and not arr[j][k] and not arr[i][k]:
                cnt += 1

print(cnt)