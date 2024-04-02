# 플로이드
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = []
for _ in range(M):
    s, e, c = map(int, input().split())
    arr.append((c, s, e))
