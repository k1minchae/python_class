# 가장 큰 사각형 그리기
from itertools import permutations
arr = list(map(int, input().split()))
X = list(permutations(arr, 4))

max_area = 0
for x in X:
    area = min(x[0], x[1]) * min(x[2], x[3])
    max_area = max(max_area, area)

print(max_area)