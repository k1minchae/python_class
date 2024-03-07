# 구간의 합(low)
'''
input
10 5
1 2 3 4 2 5 3 1 1 2

output
3
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for low in range(N):
    for high in range(low, N):
        if sum(arr[low:high]) == M:
            cnt += 1
print(cnt)

'''
강사님 코드
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt, sum = 0, 0
high, low = 0, 0
while True:
    if sum >= M or high == N:   # 범위 좁히기
        sum -= arr[low]
        low += 1
    elif sum < M:   # 합이 원하는 합보다 작다면 (넓히기)
        sum += arr[high]
        high += 1
    if sum == M:
        cnt += 1
    if low == N: break
print(cnt)