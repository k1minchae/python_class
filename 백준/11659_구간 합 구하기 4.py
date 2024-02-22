# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0] * len(arr)
sum_arr[0] = arr[0]
for i in range(1, len(arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for _ in range(M):
    x, y = map(int, input().split())
    if x == 1:
        result = sum_arr[y-1]
    else:
        result = sum_arr[y-1] - sum_arr[x-2]
    print(result)