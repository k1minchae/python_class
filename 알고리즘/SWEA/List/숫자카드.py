T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    max_v = max(a) # 카드중 가장 큰 숫자
    arr = [0] * (max_v + 1)
    cnt = [0] * (max_v + 1)

    count = 0
    for i in a:
        cnt[i] += 1

    max_c = max(cnt) # 가장 많이 카운트 된 카운트 값
    count = 0
    for i in range(N-1, 0, -1):
        if cnt[i] == max_c:
            count = i


    print(f'#{tc} {count} {max_c}')

