# 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def kill(y, x):
        if 0 > y or 0 > x or x >= N or y >= N:
            return 0

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N-M+1):

