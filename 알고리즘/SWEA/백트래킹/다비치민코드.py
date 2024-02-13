# 다비치 민코드
from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
M_arr = list(combinations(arr, M))
min_v = float('inf')
result = ()
for i in M_arr:
    cal = 1
    for j in i:
        cal *= j
    if cal < min_v:
        min_v = cal
        result = i
result = sorted(result)
print(*result)