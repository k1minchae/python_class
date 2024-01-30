T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 충전당 갈수있는 거리, N: 종점정류장, M: 충전기 개수
    charge_spot = list(map(int, input().split()))

    bus_stop = [0] * (N + 1)
    M_number = [0] * (N + 1) # 충전기가 있으면 1 없으면 0
    bus_location = [0] * (N + 1)

    for idx in charge_spot:
        M_number[idx] = 1
        if K // idx == 1:
            bus_location[idx] += 1
        elif K // idx == 
    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    for idx, stop in M_number:
        if 2 * K < idx