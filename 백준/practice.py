# 세 용액
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

val = float('inf')
result = (0, 0, 0)
for i in range(N):
    start = i+1
    end = N-1
    while start < end:
        v = arr[start] + arr[end] + arr[i]
        if v == 0:
            print(arr[i], arr[start], arr[end])
            exit(0)
        if abs(v) < abs(val):
            val = v
            result = (arr[i], arr[start], arr[end])
        if v < 0:
            start += 1
        else:
            end -= 1
print(*result)