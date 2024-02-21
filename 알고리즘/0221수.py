# 이진 탐색

# def bst(n):
#     global node
#     if n <= N: # 전체 노드의 수 N보다 작거나 같을 때
#         bst(n * 2)  # 왼쪽 자식 노드로 이동
#         tree[n] = node
#         node += 1
#         bst(n * 2 + 1) # 오른쪽 자식 노드로 이동
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     node = 1
#     bst(1)
#     print(f'{tc} {tree[1]} {tree[N // 2]}') # 루트값,  N // 2번 노드값

# 이진 힙
# 마지막 노드의 조상노드의 합 구하기
# import heapq
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = []
#     nums = list(map(int, input().split()))
#     for num in nums:
#         heapq.heappush(tree, num) # 힙에 숫자를 추가하면서 자동 정렬
#
#     sum_v = 0 # 구하려는 값
#     N = len(tree) // 2 # 마지막 노드의 부모 노드 인덱스 계산
#     while N:
#         sum_v += tree[N-1] # 조상노드의 값 더하기
#         # 부모노드로 올라가기
#         N //= 2
#     print(f'#{tc} {sum_v}')
#
#
#
#
# 노드의 합
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#     for _ in range(M):
#         idx, value = map(int, input().split()) # 리프노드 값
#         tree[idx] = value
#     for i in range(N, 0, -1):   # 노드의 개수부터 1까지 역순 순회
#         if i // 2 > 0: # 부모 노드의 인덱스가 0보다 크면
#             tree[i // 2] += tree[i] # 부모 노드에 자식 노드의 값을 더함
#     result = tree[L]
#
#     print(f'#{tc} {result}')

# 중계기

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     area = [list(map(int, input().split())) for _ in range(N+1)]
#     least_R = 0
#     hi = hj = 0 # 중계기 좌표
#     lst = []
#     for i in range(N+1):
#         for j in range(N+1):
#             if area[i][j] == 1:
#                 lst.append([i, j])
#
#             if area[i][j] == 2:
#                 hy, hj = i, j
#
#     for l in lst:
#         radius = ((l[0] - hi) ** 2 + (l[1] - hj) ** 2) ** 0.5  # 반지름
#         least_R = max(radius, least_R)
#         result = math.ceil(least_R)
#     print(f'#{tc} {result}')


# 두개의 직사각형
T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 1001 for _ in range(1001)]
    cnt = [0] * 5
    for _ in range(2):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(y1, y2+1):   # 사각형 테두리 또는 사각형의 내부
            for k in range(x1, x2+1)
                if j == y1 or j == y2 or k == x1 or k == x2:
                    arr[j][k] += 1
                arr[j][k] += 1
                cnt[arr[j][k]] += 1 # 각 영역의 카운트 업데이트
    if cnt[4] == 1:
        ans = 3
    elif cnt[4] > 1 and cnt[3] > 0:
        ans = 1
    elif cnt[4] > 1:
        ans = 2
    else:
        ans = 4
    print(f'#{tc} {ans}')