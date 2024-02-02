# 전기버스

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    curr, cnt = 0, 0 # curr: 현위치, cnt : 충전횟수
    while curr != N: # 종점에 도착할 때까지 반복
        if N <= curr + K # 한번 충전으로 갈 수 있는 거리가 종점까지의 거리보다 길면
            curr = N # 현위치는 N이고 반복중단
            break

        # 충전소 뒤에서부터 순회
        for i in range(len(arr) - 1, -1, -1):
            # 리스트 arr 의 값이 한번 충전으로 갈 수 있는 거리 이내에 있다면
            if arr[i] <= curr + K:
                cnt += 1  #충전횟수 증가
                curr = arr[i] # 현위치를 충전소 위치로 변경
                arr = arr[i + 1 :] # 해당 충전소 이후의 정류장만 남기기
                break
            if i == 0: # 충전소를 찾지 못 함
                cnt = 0
                curr = N # 현위치를 종점으로

    print(f'#{tc} {cnt}')


# 폭탄 투하
arr = [['_' for _ in range(5)] for _ in range(4)]
for _ in range(2):
    y, x = map(int, input().split())
    dy = [-1, -1, -1, 0, 1, 1, 1, 0] # 경우의수 8개
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(8): # 경우의수 8개 (상하좌우 대각선)
        # 다음 y = ny
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny > 3 or nx >4:
            continue # 방향 벗어났을때
        arr[ny][nx] = '#'

for row in arr:
    print(*row)

continue 안쓰고 해보기
방향 tuple로 묶어보기
