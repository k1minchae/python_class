# 1860. 진기의 최고급 붕어빵
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 손님수 N, M초당, K개 만듦
    arr = sorted(list(map(int, input().split())))
    sold_bread = 0
    def F():
        global sold_bread
        for time in arr:
            bread = (time // M) * K - sold_bread
            if bread >= 1:
                sold_bread += 1
            else:
                return 'Impossible'
        return 'Possible'
    print(f'#{tc} {F()}')

# 강사님 코드
def start():
    sold_bread = 0
    for person in customers:
        # 특정 시간에 빵을 만들수 있는 개수
        made_bread = (person // m) * k

        # 빵을 하나 팜
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread

        if remain < 0:
            return 'Impossible'
    return 'Possible'