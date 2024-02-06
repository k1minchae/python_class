T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    check = 0
    for i in range(N):
        cnt = 0
        for j in range(N-M//2+1):
            if arr[i][j:j+M//2] == arr[i][j+M-1:j+M-M//2-1:-1]:
                check = 1
                print(f'#{tc} ', *arr[i][j:j+M-1], sep ='')
            else:
                continue

    if check != 1:
        for i in range(N):
            cnt = 0
            for j in range(N - M // 2 + 1):

                    check = 1
                    print(f'#{tc} ', end = '')
            for j in range(N):
                print(arr[j:j + M - 1][i], end = '')
            else:
                continue
