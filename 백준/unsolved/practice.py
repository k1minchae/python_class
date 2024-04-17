# 용액
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = N-1
min_v = arr[start] + arr[end]
result = (0, N-1)
while start < end:
    val = arr[start] + arr[end]
    if abs(val) < abs(min_v):
        result = (start, end)
        min_v = val

