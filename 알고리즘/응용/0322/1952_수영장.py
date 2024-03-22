# 수영장 (DP)

T = int(input())
for tc in range(1, T+1):
    day, one_month, three_month, year = map(int, input().split())
    plans = [0] + list(map(int, input().split()))

    DP = [0] * 13

    # 1~12월까지 반복
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 전 달 + 1일권 구입 / 전 달 + 1달권 구입 / 3달전 + 3달권 구입
        DP[i] = DP[i-1] + min(plans[i] * day, one_month)
        if i >= 3:
            DP[i] = min(DP[i], DP[i-3] + three_month)

    print(f'#{tc}', DP[-1])