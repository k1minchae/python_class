import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input().strip())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# 전봇대 A를 기준으로 정렬
arr.sort()

# LIS를 찾기 위한 배열, 전봇대 B의 값을 기준으로 함
lis = []
# 각 원소가 LIS의 어느 위치에 해당하는지 저장하기 위한 배열
position = [0] * N

for i in range(N):
    # arr[i][1]이 lis 배열에서 들어갈 위치 찾기
    idx = bisect_left(lis, arr[i][1])
    # 만약 lis의 마지막 값보다 크다면 교차X 이므로 추가
    if idx >= len(lis):
        lis.append(arr[i][1])
    else: # 교차 한다면 현재 전깃줄 기준으로 갱신
        lis[idx] = arr[i][1]  # idx의 위치를 arr[i][1]으로 갱신
    position[i] = idx  # arr[i]의 값이 lis의 몇 번째 위치에 해당하는지 저장

# LIS에 포함되지 않는 전깃줄의 개수 출력
print(N - len(lis))

# LIS에 포함되지 않는 전깃줄 찾아서 출력
# LIS를 추적하기 위해 거꾸로 탐색 시작
lis_length = len(lis) - 1
for i in range(N - 1, -1, -1):
    if position[i] == lis_length: # lis의 해당되는 마지막 값 찾음
        lis_length -= 1 # 그 다음 마지막 값 찾으러
    else:
        # LIS에 포함되지 않으면 출력
        print(arr[i][0])
