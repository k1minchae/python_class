# 전깃줄
import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))

lis = [] # 최장 증가 부분 수열
for i in range(N):
    idx = bisect_left(lis, lst[i])
    if len(lis) <= idx: # 교차 안 한다면 수열 + 1 이므로
        lis.append(lst[i]) # LIS 에 해당 원소 추가

    else: # 교차 한다면 교차 하는 부분 교체
        lis[idx] = lst[i]

print(N - len(lis))