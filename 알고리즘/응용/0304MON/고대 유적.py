# 고대 유적

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_d = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt +=1
                if cnt >= max_d:
                    max_d = cnt
            else:
                if cnt >= max_d:
                    max_d = cnt
                cnt = 0

    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
                if cnt >= max_d:
                    max_d = cnt
            else:
                if cnt >= max_d:
                    max_d = cnt
                cnt = 0
    print(f'#{tc} {max_d}')