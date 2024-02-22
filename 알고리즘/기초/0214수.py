# def f(i, k, t): # k 개의 원소를 가진 배열 A , 부분집합의 합이 t 인경우
#     if i == k: # 모든 원소에 대해 결정하면
#         ss = 0  # 부분집합의 합
#         for j in range(k):
#             if bit[j]:  # A[j] 가 포함된 경우
#                 # print(A[j], end = ' ')
#                 ss += A[j]
#         if ss == t: # 합이 t라면
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end = ' ')
#             print()     # 하나의 부분집합 출력 완료
#     else:
#         # for j in range(1, -1, -1): # 1 하고 0 넣는 반복문
#         #     bit[i] = j
#         #     f(i+1, k)
#         bit[i] = 1
#         f(i+1, k, t)
#         bit[i] = 0
#         f(i+1, k, t)
#
# N = 10
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * N   # A[i]가 부분집합에 포함되는지 표시
# f(0, N, 10)


토너먼트 카드게임

def TNT(start, end):
    if start == end:
        return start # 부전승
    a = TNT(start, (start+end) // 2)    # 첫번째 그룹
    b = TNT((start + end) //2 + 1, end) # 두번째 그룹
    return RSP(a, b)

def RSP(x, y):
    if cards[x] ==cards[y]: # 비긴경우
        return x
    # x승리
    elif cards[x] - cards[y] == 1 or cards[x] - cards[y] == -2:
        return x
    else:
        return y

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = TNT(0, N-1) + 1
    print(f'#{tc} {result}')



# 배열 최소합
# used -> 가지치기

def min_v(idx, now_sum):
    global min_sum
    if now_sum >= min_sum: # 현재 합이 최소 합보다 크면 탐색X
        return
    if idx == N:    # 모든 행을 선택했으면, 현재 합과 최소합을 비교
        if min_sum >now_sum:
            min_sum = now_sum
            return
    for i in range(N):  # 현재 행에서 모든 열 순회
        if not used[i]:
            used[i] = 1 # 해당 열 사용표시
            min_v(idx+1, now_sum + arr[idx][i])
            used[i] = 0     # 복구 (백트래킹)
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = float('inf')
    min_v(0, 0)
    print(f'#{tc} {min_sum}')