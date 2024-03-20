# # 그룹나누기
# from collections import deque
#
# # 인접 리스트를 전부 탐색해서 visited를 통해 그룹표시
# def BFS(start):
#     q = deque([start])
#     visited[start] = 1
#     while q:
#         node = q.popleft()
#         if adj[node]:
#             for next in adj[node]:
#                 if not visited[next]:
#                     q.append(next)
#                     visited[next] = 1
#
# # 입력받음
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     # 인접리스트 만들기
#     adj = [[] for _ in range(N+1)]
#     for i in range(0, 2 * M - 1, 2):
#         adj[arr[i]].append(arr[i+1])
#         adj[arr[i+1]].append(arr[i])
#
#     # 결과 출력
#     result = 0
#     visited = [0] * (N+1)
#     for i in range(1, N+1):
#         if not visited[i]: # 어디도 속해있지 않는다면 새로운 그룹 추가해야함
#             result += 1 # 그룹의 수
#             BFS(i) # BFS 돌려서 그룹화 해주기
#
#     print(f'#{tc} {result}')

def find_set(x):
    # 아래와 같은 코드는 뭐가 문제일까?
    #  == 대표자가 아닌 연결된 부모노드를 출력
    #  == 제대로된 대표자 데이터를 출력하지 않는다!
    # return parents[x]

    # 기저조건: 대표자가 자기 자신일 때 종료
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    # 아래 처럼 바로 초기화를 하면
    # 싸이클이 발생할 수 있다.
    # parents[y] = x

    # 싸이클 발생 막기-------------------------
    # x 와 y 의 대표자를 찾아서
    x = find_set(x)
    y = find_set(y)

    # x 와 y 의 대표자가 같다
    # == 이미 같은 집합에 속해있다.
    # ==> 그러면 아무 행동 안함
    if x == y:
        return

    # 대표자를 바꾸는 기본 코드
    # parents[y] = x

    # 문제 조건에서 "낮은 번호를 대표자로 만들어라" 라는 내용들이 추가되면
    # 아래처럼 조건문을 작성
    # if x < y:
    #     parents[y] = x
    # else:
    #     parents[x] = y


    # 랭크를 이용한 union
    # y가 덩치가 더 큰 집합이면 x -> y 쪽에 이동
    # if ranks[x] < ranks[y]:
    #     parents[x] = y
    # elif ranks[y] < ranks[x]:
    #     parents[y] = x
    # else:
    #     parents[y] = x
    #     ranks[x] += 1



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))

    # 예시로 N = 5
    # 아무 행동도 하지 않았을 때, 집합은 몇 개 인가?
    # 자기자신이 대표인 그룹을 N + 1 개 생성: make_set
    parents = list(range(N + 1))
    # 효율적 연산을 위한 rank 리스트 만들기
    ranks = [0] * (N+1)

    for i in range(0, len(li), 2):
        union(li[i], li[i + 1])

    cnt = 0
    # 대표자의 수만 count
    for i in range(1, len(parents)):
        # 인덱스 == 자기 자신 번호가 들어있으면, 해당 그룹의 대표자
        if i == parents[i]:
            cnt += 1

    print(f'#{tc} {cnt}')



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 예시로 N = 5
    # 아무 행동도 하지 않았을 때 집합은 몇 개인가 ?
    # 자기 자신이 대표인 그룹을 N + 1개 생성 : make_set
    parents = list(range(N+1))