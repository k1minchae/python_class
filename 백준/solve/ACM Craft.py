# ACM Craft
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    times = list(map(int, input().split()))
    cnt_lst = [0] * N # 위상을 저장할 리스트
    adj = [[]for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x-1].append(y-1)
        cnt_lst[y-1] += 1
    tar = int(input()) # 목표 정점
    q = deque([]) # 위상이 0인것부터 저장하고 시작 -> 건설한 것들 저장
    result = [0] * N # 걸리는 시간을 저장할 배열
    for i in range(N):
        if cnt_lst[i] == 0:
            q.append(i)
            result[i] = times[i]

    while q:
        x = q.popleft()
        if x == tar - 1: # 목표지점에 도착했다면
            print(result[tar-1]) # 결과 출력후 break
            break
        for nx in adj[x]: # 다음정점 탐색
            cnt_lst[nx] -= 1 # 위상 -1
            result[nx] = max(result[x] + times[nx], result[nx]) # 최대값으로 갱신
            if cnt_lst[nx] == 0: # 위상이 0이라면 건설가능
                q.append(nx) # 큐에 추가 -> 건설