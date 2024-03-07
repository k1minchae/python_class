# 슬라이딩 윈도우(low)
# 내 코드
T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = sum(arr[0:W])
    sum_v = sum(arr[0:W])
    idx_left = 0
    idx_right = W-1
    for i in range(1, N-W+1):
        sum_v += arr[i+W-1]-arr[i-1]
        if max_sum < sum_v:
            max_sum = sum_v
            idx_left = i
            idx_right = i+W-1
    print(f'#{tc} {idx_left} {idx_right} {max_sum}')


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    end = m-1
    sum_v = 0
    for i in range(end): # 처음 윈도우의 합
        sum_v += arr[i]
    ans = float('-inf')
    s_idx = 0
    e_idx = 0
    while end < n:  # 윈도우의 끝이 피사체개수를 벗어나지 않도록
        sum_v += arr[end]   # 윈도우 끝에 해당하는 피사체 합에 추가
        if sum_v > ans:
            ans = sum_v
            s_idx = start
            e_idx = end
        sum_v -= arr[start]   # 윈도우 시작에 해당하는 피사체 합에 제거
        start += 1
        end += 1
    print(f'#{tc} {s_idx} {e_idx} {ans}')

'''
예제 : n 개의 정수를 입력받고 연속된 m개의 정수들의 합을 구할 때 최대값 구하기.
합이 가장 큰 구간의 값은 무엇일까요 ?

input
10 2
3 -2 -4 -9 0 3 7 13 8 -3

output
21
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_v = 0

# 처음 m개의 정수들의 합
for i in range(m):
    sum_v += arr[i]
    max_v = sum_v

# n-m번 반복 ( 슬라이딩 윈도우를 이동시키며 계산 )
for i in range(n-m):
    # 1. 윈도우를 한 칸 오른쪽으로 이동시키고 그 값을 더함
    # 2. 이전 값을 빼준다.
    sum_v += arr[i+m]
    sum_v -= arr[i]
    if sum_v > max_v:
        max_v = sum_v
print(max_v)

