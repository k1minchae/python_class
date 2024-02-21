# 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]
arr2 = [input() for _ in range(M)]

result = list(set(arr1) & set(arr2))
result.sort()
print(len(result))
print(*result, sep = '')