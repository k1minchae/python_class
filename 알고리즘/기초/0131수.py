# 색칠하기

# 1번 풀이 : 1과 2가 겹치면 3 -> 3을 카운트
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)] # 10 x 10 2차원리스트
    cnt = 0
    for k in range(N):
        r1, b1, r2, b2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(b1, b2 + 1):
                arr[i][j] += color

                # 격자 값이 3이면 카운팅
                if arr[i][j] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')
    # 문제점 : red가 3번 겹치면 3이라서 문제가 발생한다. -> 보라색 영역만 정확히 카운트 해야함


# 2번 풀이 : 정확히 보라색만 카운트 (이걸로 하기!)
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 색에 따른 카운트 리스트
    r_list = []
    b_list = []
    cnt = 0

    for k in range(N):
        r1, b1, r2, b2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(b1, b2 + 1):
                if color == 1:
                    r_list.append([i, j]) # 각 좌표를 리스트에 추가
                if color == 2:
                    b_list.append([i, j])

    # 공통인 것들만 카운트
    for cm in r_list:
        cnt += b_list.count(cm)

    print(f'#{tc} {cnt}')
'''

# 부분집합의 합 풀이

'''모듈쓰는법
import itertools
lst = [1, 2, 3]
# lst의 순열
result1 = list(itertools.combinations(lst, 3))
# combinations(lst, N) : lst 에서 N개의 원소를 가진 모든 조합 (중복X)
result2 = list(itertools.combinations(lst, 2))
print(result2)
'''

import itertools

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    list_comb = itertools.combinations(lst, N)
    cnt = 0

    for i in list_comb:
        if sum(i) == K:
            cnt += 1
    print(f'#{tc} {cnt}')

모듈 안 쓰고 풀이

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    cnt = 0

    for i in range(1 << 12): # lst 의 요소 개수가 12개이므로
        sum_sub = 0  # 부분집합의 원소 합계
        subset = []  # 현재 부분 집합

        for j in range(12):  # 집합의 각 원소에 대해 반복
            if i & (1<<j):  # i의 이진 표현에서 j 번째의 비트가 1인지 아닌지 판단
                sum_sub += lst[j]  # 부분집합의 합계 갱신
                subset.append(lst[j])  # 부분집합에 원소 추가

        if len(subset) == N and sum_sub == K:
            cnt += 1

    print(f'#{tc} {cnt}')

'''
마법사의 사냥
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    sum_v = 0

    # 마법의 방향 (대각선 네방향)
    for i in range(4):
        # 마법의 파워 (현위치 : (i, j) 제외)
        for j in range(1, K + 1):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum_v += arr[ny][nx]

    return sum_v

sum_list = [magic(i, j) for i in range(N) for j in range(N)] # 중첩 for 문안에서 함수 호출
print(max(sum_list))

'''
폭탄 터뜨리기
'''

def bomb(N, M, K, arr):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                arr[i][j] = '%'
                for d in range(4):
                    for k in range(1, K + 1):
                        ny = i + dy[d] * k
                        nx = j + dx[d] * k
                        if 0 <= ny < N and 0 <= nx < M:
                            # 두가지의 경우를 나눠서
                            if arr[ny][nx] == '_':
                                arr[ny][nx] = '%'
                            if arr[ny][nx] == '#':
                                break

N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

bomb(N, M, K, arr)
print(arr)
# for row in arr:
#     print(*row, sep = '') # 공백 없이 출력하라는 뜻