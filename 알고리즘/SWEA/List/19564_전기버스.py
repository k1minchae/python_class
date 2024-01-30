T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 충전당 갈수있는 거리, N: 종점정류장, M: 충전기 개수
    arr = list(map(int, input().split())) # 충전기 위치

    curr = 0 # 현위치
    count = 0 # 충전횟수

    while curr != N+1:
        if curr + K >= N:
            curr = N
        else:
            for i in range(len(arr)-1, -1, -1):
                if arr[i] <= curr + K:
                    curr = arr[i]
                    count += 1
                    arr = arr[i+1:]
                else:
                    count = 0

    print(count)
