# 여행 가자
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parents[x] = y
    elif rank[y] < rank[x]:
        parents[y] = x
    else:
        rank[x] += 1
        parents[y] = x

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split())) # 여행계획 리스트

parents = [i for i in range(N+1)] # 부모 리스트 (초기값 : 자기 자신)
rank = [0] * (N+1) # (랭크 저장)

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            arr[j][i] = 0 # 중복 방지를 위해 반대편에 있는 1 지워줌
            union(i+1, j+1) # 연결된 것을 같은 집합으로 합친다.

'''아래 노드에는 아직 조상노드(찐대표자) 반영이 안되어있을 수 있으므로 순회하면서 갱신해줌'''
for i in range(N+1):
    find(i)

result = 'YES' # 결과 초기값 : YES
val = 0
for city in plan:
    if val == 0: # 아직 값이 저장 안되어있다면 값 저장
        val = parents[city]
    else: # 앞서 방문한 도시의 부모랑 다른 경우 NO 반환
        if parents[city] != val:
            result = 'NO'
            break
print(result)