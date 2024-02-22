# 피보나치 수 DP적용 알고리즘
# def fibo(n):
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i-1] + f[i-2]
#
#     return f[n]
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(i, V): # 시작 번호 : i , 마지막 : V
    # visited, stack 생성 및 초기화
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1 # 시작점 방문
    print(i)  # 시작점 출력

    # 현재 정점에 인접하고 방문안한 정점w 가 있으면
    while True: # 탐색
        for w in adjl[i]: # 인접리스트를 탐색했을 때
            if visited[w] == 0: # 방문 안한 정점이라면
                stack.append(i) # push : i를 거쳐서
                i = w      # w에 방문
                visited[i] = 1 # 방문해서 할 일
                print(i)
                break   # for w 를 중단시키는 break
        else: # for else : 반복문이 완료되고도 break가 안됐을때
            # 스택이 비어있지 않으면 ( 지나온 정점이 남아있으면 )
            if stack:
                i = stack.pop()
            else: # 스택이 비어있으면 (출발점까지 거슬러 올라갔다면)
                break # while 탐색 마무리

    return # while 이 끝나면 함수 끝내기

V, E = map(int, input().split()) # 마지막 정점 번호 V
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # arr[i] 행에 i에 인접인 노드번호 (0~7)
for i in range(E): # 두개씩 끊어서 읽어오기
    node_1, node_2 = arr[i*2], arr[i*2+1]
    adjl[node_1].append(node_2)
    adjl[node_2].append(node_1) # 양방향이기 때문에 서로 추가해줘야 함
# print(adjl)
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
dfs(1, V) # 1번부터 V까지 탐색
# 1 2 4 6 5 7 3




 # 재귀로 푸는법

def dfs(i): # 시작 번호 : i , 마지막 : V
    visited[i] = 1 # 방문표시
    print(i)
    # i 에 인접하고 방문안 한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)    # 한번 더 실행


V, E = map(int, input().split()) # 마지막 정점 번호 V
arr = list(map(int, input().split()))
visited = [0] * (V + 1)
stack = []

# 인접리스트
adjl = [[] for _ in range(V+1)] # arr[i] 행에 i에 인접인 노드번호 (0~7)
for i in range(E): # 두개씩 끊어서 읽어오기
    node_1, node_2 = arr[i*2], arr[i*2+1]
    adjl[node_1].append(node_2)
    adjl[node_2].append(node_1) # 양방향이기 때문에 서로 추가해줘야 함
# print(adjl)
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
dfs(1) # 1번부터 탐색
# 1 2 4 6 5 7 3
'''

# visited 배열 : 노드가 방문했는지 여부를 True 또는 False로 저장
# 무한루프 방지, 이미 방문한 노드를 다시 방문하지 않도록
