# 14713 : 앵무새
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [deque(list(input().split())) for _ in range(N)]
L = list(input().split())
lst = [[] for _ in range(N)]
