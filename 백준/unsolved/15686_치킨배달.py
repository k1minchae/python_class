# 치킨 배달
import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken = []    # 치킨의 좌표 받기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j]) # y, x
all_ck_case = list(combinations(chicken,M)) # M 까지의 모든 치킨 경우의수

min_sum = float('inf')
def DFS(chicken_lst):
    global min_sum
    d_sum = 0
    if min_sum < d_sum:  # 가지치기
        return
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 집 발견
                d = float('inf')
                for ck_y, ck_x in chicken_lst:
                    d = min(abs(i - ck_y) + abs(j - ck_x), d)
                d_sum += d
    min_sum = min(min_sum, d_sum)

for case in all_ck_case:
    DFS(case)

print(min_sum)