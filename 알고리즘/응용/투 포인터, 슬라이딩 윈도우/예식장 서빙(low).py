# 예식장 서빙(low)
# 내 코드
T = int(input())
for tc in range(1, T+1):
    N, R = map(int, input().split())
    arr = list(map(int, input().split()))

    def eat():
        for i in range(N):
            food = {}
            food[arr[i]] = 1
            for r in range(1, R+1):
                food[arr[(i+r)%N]] = food.get(arr[(i+r)%N], 0) + 1
                if food[arr[(i+r)%N]] >= 3:
                    return 'NO'
            for r in range(-R, 0):
                food[arr[i+r]] = food.get(arr[(i+r)], 0) + 1
                if food[arr[(i+r)]] >= 3:
                    return 'NO'
        return 'YES'

    print(f'#{tc} {eat()}')

# 강사님 코드
T = int(input())
for tc in range(1, T+1):
    arr = [0] * 200002
    DAT = [0] * 201 # 번호가 나온 횟수
    n, r = map(int, input().split())
    foods = list(map(int, input().split()))

    for i in range(n):
        arr[i] = foods[i]   # 해당 자리에 앉은 손님이 먹을 음식의 번호
        arr[i + n] = foods[i]  # 끝과 시작이 이어지는 원형탁자이므로.

    start = 0    # 윈도우의 시작
    end = 2 * r  # 윈도우의 끝
    flag = False # 중복 여부를 체크

    for k in range(start, end):
        DAT[arr[k]] += 1
        if DAT[arr[k]] > 2: # 중복된 음식이 3 이상 있을 경우
            flag = True
            break
    while end < n * 2 and flag == 0:    # 윈도우를 이동하면서 중복된 음식이 있는지 확인
        DAT[arr[end]] += 1  # 끝부분 해당 음식 추가
        if DAT[arr[end]] > 2:
            flag = True
            break
        DAT[arr[start]] -= 1

        # 윈도우를 오른쪽으로 이동
        start += 1
        end += 1
    if flag:
        print(f'#{tc} {"NO"}')
    else:
        print(f'#{tc} {"YES"}')