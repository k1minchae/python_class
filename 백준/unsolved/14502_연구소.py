import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 바이러스 : 2, 벽: 1, 빈칸: 0
