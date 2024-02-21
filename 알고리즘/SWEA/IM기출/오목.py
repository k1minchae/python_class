def find(y, x):
    # 가로
    cnt_h = 0
    for j in range(N):
        if arr[y][j] == 'o':
            cnt_h += 1
        else:
            cnt_h = 0
        if cnt_h == 5:
            return True

    # 세로
    cnt_v = 0
    for i in range(N):
        if arr[i][x] == 'o':
            cnt_v += 1
        else:
            cnt_v = 0
        if cnt_v == 5:
            return True

    # 대각 (우하향)
    cnt_c = 0
    for k in range(-4, 5):
        if 0 <= y + k < N and 0 <= x + k < N:
            if arr[y+k][x+k] == 'o':
                cnt_c += 1
            else:
                cnt_c = 0
            if cnt_c == 5:
                return True

    # 대각 (우상향)
    cnt_c = 0
    for k in range(-4, 5):
        if 0 <= y - k < N and 0 <= x + k < N:
            if arr[y - k][x + k] == 'o':
                cnt_c += 1
            else:
                cnt_c = 0
            if cnt_c == 5:
                return True

def final():
    for Y in range(N):
        for X in range(N):
            check = find(Y, X)
            if check:
                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = final()
    print(f'#{tc} {result}')
