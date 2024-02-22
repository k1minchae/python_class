# 이사
# from collections import deque
#
# def bfs(node):
#     global cnt
#     q = deque([node])
#     visited[node] = 1
#     while q:
#         now = q.popleft()
#
#         if visited[now] - 1 <= k:
#             cnt += 1
#         if visited[now] -1 > k: # 탐색 X
#             break
#         for i in range(1, n+1):
#             if arr[now][i] == 0 or visited[i] > 0:
#                 continue
#             visited[i] = visited[now] + 1
#             q.append(i)
#
# n, m = map(int, input().split()) # 지역수, 버스 노선 수
# arr = [[0] * (n+1) for _ in range(n + 1)]
# visited = [0] * (n + 1)
# cnt = 0
#
# for _ in range(m):
#     node1, node2 = map(int, input().split())
#     arr[node1][node2] = 1   # node1 에서 node2로 가는 경로 표시
#     arr[node2][node1] = 1   # 양방향
#
# r, k = map(int, input().split()) # 회사, 탑승 횟수
#
# bfs(r)
# print(cnt)

