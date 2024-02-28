#  화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # [시작, 종료]
    arr.sort(key = lambda x: x[1])

    cnt = 0
    end = 0
    for car in arr:
        s = car[0]
        e = car[1]
        if end > s:
            continue
        end = e
        cnt += 1
    print(f'#{tc} {cnt}')
