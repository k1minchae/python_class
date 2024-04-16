# 줄세우기
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
cnt_lst = [0] * N # 앞에 세워야하는 사람수 세어두는 리스트
adj = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    cnt_lst[b-1] += 1 # b앞에 a가 서야함

q = deque([])
result = [] # 줄 세운 사람들을 저장할 결과 리스트
visited = [0] * N # 이미 줄세운애들을 확인할 visited 배열

# cnt_lst 를 순회해서 앞에 세워야하는 애 없으면 일단 줄세우자 (q와 result에 추가)
for i in range(N):
    if not cnt_lst[i]:
        q.append(i)
        visited[i] = 1
        result.append(i+1)

def f():
    while q:
        x = q.popleft()
        # x 뒤에 설 수 있는 애들을 탐색함
        for n in adj[x]:
            if not visited[n]: # 아직 줄 안세운 애들만 탐색
                # x가 앞에 섰으니 cnt_lst 에서 -1 해줌
                cnt_lst[n] -= 1
                if not cnt_lst[n]: # 앞에 더 세워야하는 애가 없다면
                    q.append(n) # 큐에 추가하고
                    result.append(n+1) # 줄 세우고
                    visited[n] = 1 # 방문표시도 해줌

f()
print(*result)