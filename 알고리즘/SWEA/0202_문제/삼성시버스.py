T = int(input())
for tc in range(1, T+1):
    bus_dict = {}
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus_dict[i] = bus_dict.get(i, 0) + 1
    P = int(input())
    P_list = []
    for p in range(P):
        c = int(input())
        P_list.append(c)
    result = []
    for i in P_list:
        result.append(bus_dict.get(i,0))
    print(f'#{tc}',end=' ')
    print(*result)