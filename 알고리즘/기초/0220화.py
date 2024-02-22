# subtree
# def sub_tree(node):
#     global cnt
#     for i in range(2): # 왼쪽 자식, 오른쪽 자식
#         if tree[i][node]:   # 해당 노드에 자식이 있다면
#             cnt += 1
#             n = tree[i][node]
#             sub_tree(n)  # 자식 노드에 대해 재귀 호출
#
# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int, input().split())
#     temp = input().split()
#
#     # 이진트리 리스트 초기화 -> 노드번호 1번부터 E+1 번까지
#     tree = [[0 for _ in range(E + 2)] for _ in range(2)]
#     for i in range(E):
#         p_node = int(temp[2 * i]) # 부모노드 : 짝수번째
#         c_node = int(temp[2 * i + 1])
#         if not tree[0][p_node]:
#             tree[0][p_node] = c_node    # 왼쪽에 자식이 없으면 왼쪽에 할당
#         else:
#             tree[1][p_node] = c_node    # 있으면 오른쪽에 할당
#     cnt = 1
#     sub_tree(N)
#     print(f'#{tc} {cnt}')
#
# 여기서부터 IM 기출
# captcha code
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#     result = 1
#
#     for i in range(len(passcode)):
#         now = passcode[i]
#
#         try:
#             index = sample.index(now)
#             sample = sample[index + 1:]
#         except:
#             result = 0
#     print(f'#{tc} {result}')



# 사각형 그리기 게임
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_area = 0
#     cnt = 0
#
#     for y in range(N):
#         for x in range(N):
#             cur = arr[y][x] # 왼쪽 위의 좌표값
#             for ny in range(y, N):
#                 for nx in range(x, N):
#                     if arr[ny][nx] == cur:  # 동일한 값을 만나면
#                         area = (ny - y + 1) * (nx - x + 1)
#                         if area > max_area:
#                             max_area = area
#                             cnt = 1     # 최대값 갱신시 cnt 초기화
#                         elif area == max_area: # 같은 크기 면적 있을 시 누적
#                             cnt += 1
#
#     print(f'#{tc} {cnt}')


#