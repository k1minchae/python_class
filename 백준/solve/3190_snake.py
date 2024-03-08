# 뱀
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())    # 맵 크기
K = int(input())    # 사과 개수

arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1] = b - 1

command = deque([])
L = int(input())
for _ in range(L):
    s, c = input().split()
    command.append([int(s), c])

dir = [(1, 0), (0, -1), (-1, 0), (1, 0)]  # 우회전
def BFS():
    sec = 1
    next_sec, comd = command.popleft()
    snake = deque([[0, 0]]) # 몸의 좌표
    x, y = 1, 0    # 머리의 좌표

    while snake:


