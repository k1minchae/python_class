# 가로 세로
T = int(input())
for _ in range(T):
    rows, cols, K = map(int, input().split())

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    import sys

    for i in range(K):
        c_rows, c_cols = map(int, sys.stdin.readline().split())
        matrix[c_rows][c_cols] = 1

