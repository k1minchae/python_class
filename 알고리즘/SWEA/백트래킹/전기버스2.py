# 전기버스 2
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    lst = lst[1:] + [0]
    # 강사님 코드 : 정수 1개와 list 나머지
    N, *li = map(int, input().split())

    min_cnt = 10 ** 6
    def bus(idx = 0, battery = lst[0], cnt = 0):
        global min_cnt
        if idx >= N - 1:
            min_cnt = min(cnt, min_cnt)
            return
        if cnt >= min_cnt:   # 백트래킹
            return
        if battery < 0: return
        for i in range(1, battery+1):
            if battery - i < 0: break
            bus(idx + i, battery - i, cnt)
            if i + idx < N-1:
                bus(idx + i, lst[idx + i] - i, cnt + 1)

    bus()
    print(f'#{tc} {min_cnt}')

