# 용액
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1
min_v = float('inf')
result = (arr[start], arr[end])
while start < end:
    val = arr[start] + arr[end]
    if abs(min_v) > abs(val):
        min_v = val
        result = (arr[start], arr[end])
    if val == 0:
        break
    elif val > 0:
        end -= 1
    else:
        start += 1
print(*result)