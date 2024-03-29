# 카드 놓기
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
card = deque([i for i in range(1, N+1)])
result = []
for i in arr:
    if i == 3:
        result.append(card.popleft())

