T = int(input()) # 노선 수

for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # 이동가능 칸, 종점, 정류장 수
    arr = list(map(int, input().split())) # 정류장 번호 리스트
    
    cur, count = 0, 0   # 현위치, 충전횟수
    while cur != N: # 현위치가 종점이 되기 전까지 반복
        if cur + K >= N:
            cur = N
            break

        for i in range(len(arr)-1, -1, -1): # 정류장 리스트 거꾸로 순회
            if arr[i] <= cur + K:
                cur = arr[i]
                count += 1
                arr = arr[i + 1 :] # 현위치 기준 다음칸부터 정류장 다시 순회
                break

            if i == 0:
                count = 0
                cur = N

    print(f'#{tc} {count}')