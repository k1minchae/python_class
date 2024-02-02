T = int(input())
for tc in range(1, T+1):
    bus_dict = {} # 각 버스를 이동시키면서 {정류장번호: 도착횟수} 저장
    N = int(input()) # 버스 노선 개수
    for _ in range(N):
        a, b = map(int, input().split()) # 버스는 a부터 b까지 이동함
        for i in range(a, b+1): # 버스를 이동시킴
            # 정류장 도착할때마다 정류장이름: count 딕셔너리로 저장
            bus_dict[i] = bus_dict.get(i, 0) + 1

    # 주어진 모든 버스정류장의 개수
    P = int(input())
    bus_stop_list = []  # 여기에 속한 버스정류장의 도착횟수를 구해야함
    for p in range(P): 
        bus_stop = int(input()) # 도착횟수를 알고싶은 버스 정류장의 번호
        bus_stop_list.append(bus_stop)  
        
    result = []   
    
    for bus in bus_stop_list:   
        result.append(bus_dict.get(bus,0)) # 순회하면서 값이 없으면 0, 있으면 해당 value출력
    print(f'#{tc}',end=' ')
    print(*result)