# 계산기
# fx = '(6+5*(2-8)/2)'
# top = -1
# stack = [0] * 100
#
# icp = {'(': 3, '*': 2, '/':2, '+':1, '-':1} # 스택에 들어오기 전
# isp = {'(': 0, '*': 2, '/':2, '+':1, '-':1} # 스택에 들어온 후
# postfix = '' # 우리가 구하려는 후위식
# for tk in fx:
#     # 여는 괄호 push, top 원소보다 우선순위가 높으면 push
#     if tk == '(' or isp[stack[top]] < icp[tk]:
#         top += 1 # push
#         stack[top] = tk # append 로 해도 됨
#
#     # 연산자이고 top원소보다 우선순위가 높지 않으면
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
#         # top원소의 우선순위가 더 낮을 때까지 pop
#         while isp[stack[top]] >= icp[tk]:
#             top -= 1 # pop
#             postfix += stack[top+1]
#         top += 1 # push
#         stack[top] = tk
#     elif tk == ')':
#         while stack[top] != '(':
#             top -= 1 # pop
#             postfix += stack[top+1]
#         top -= 1 # 여는 괄호 pop해서 버림
#         stack[top+1]
#     else: # 피연산자인경우
#         postfix += tk
# print(postfix)

# 부분집합
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end= ' ')
#         print()
#     else:
#         # for j in range(2):
#         #     bit[i] = j
#         #     f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
# N = 4
# arr = [1, 2, 3, 4]
# bit = [0] * 4 # bit[i] : arr[i] 가 부분집합에 포함되었는지를 나타내는 배열
# f(0, N) # bit[i] 에 1 또는 0을 채우고 N 개의 원소가 결정되면 부분집합을 출력
# '''출력
#  # 공집합
# 4
# 3
# 3 4
# 2
# 2 4
# 2 3
# 2 3 4
# 1
# 1 4
# 1 3
# 1 3 4
# 1 2
# 1 2 4
# 1 2 3
# 1 2 3 4
# '''

# 후위표기법
#
# S = input()
# stack = []
#
# for s in S:
#     if '0' <= s <= '9':
#         stack.append(int(s))
#     else:
#         a = stack.pop()
#         b = stack.pop()
#         if s == '+':
#             stack.append(b+a)
#         else:
#             stack.append(b-a)
# print(stack[-1])


# 그래프 경로 - DFS

# def dfs(start, end):
#     stack = []
#     visited = [False] * (V+1)
#     stack.append(start)
#
#     while stack: # 스택이 비어있으면 반복문 종료
#         now = stack.pop()
#         visited[now] = True  # 현재 노드 방문
#         for next in range(1, V+1):
#             # 방문하지 않았고, 연결되어 있다면
#             if node[now][next] and not visited[next]:
#                 stack.append(next)
#
#     if visited[end]:  # 끝점에 방문했다면
#         return 1
#     else:
#         return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())  # V: 노드, E : 간선의 개수
#     node = [[0 for _ in range(V+1)] for _ in range(V+1)]
#     for _ in range(E):
#         start, end = map(int, input().split())
#         node[start][end] = 1 # 해당 인접 행렬에 1 할당
#     S, G = map(int, input().split()) # 출발, 도착 노드
#     result = dfs(S, G)
#     print(f'#{tc} {result}')


# 10을 만들자

# cnt = 0
#
# def func(n, level = 0, sum_v = 0):
#     global cnt
#
#     if sum_v > 10:
#         return # 더이상 진행 X
#     if level == n:  # 모든 레벨을 탐색했을 때
#         if sum_v == 10:
#             cnt += 1
#         return
#     for i in range(1, 10):
#         func(level + 1, sum_v + i, n)
#
# n = int(input())
# func(n)
# print(cnt)

# 레드마운틴

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
used = [[0 for _ in range(n)] for _ in range(n)]

def red(dy=0, dx=0):
    if dy == n-1 and dx == n-1: # 목적지에 도달
        return 1
    for dir in direction:
        ny, nx = dy + dir[0], dx + dir[1]
        if ny < 0 or nx < 0 or ny >= n or nx >= n: # 맵의 범위를 벗어나면
            continue
        if arr[ny][nx] == 1: # 장애물 있을 때
            continue
        if used[ny][nx] == 1:  # 이미 방문한 칸일 때
            continue
        used[ny][nx] = 1 # 현재 칸 방문

        result = red(ny, nx)
        if result == 1:
            return 1
        used[ny][nx] = 0  # 가지치기 -> 경로가 해결책이 아니면 방문표시 되돌리기
    return 0

used[0][0] == 1  # 시작점 방문
print(red())