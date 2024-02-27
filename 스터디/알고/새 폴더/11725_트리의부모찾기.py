# 트리의 부모 찾기
import sys
input = sys.stdin.readline

N = int(input())
tree = [[]for _ in range(N+1)]
arr = [list(map(int, input().split())) for _ in range(N-1)]

