import sys

N, M = map(int, input().split())    # 세로: N / 가로: M
castle = [list(map(str, sys.stdin.readline().strip('\n'))) for _ in range(N)]

row_count = 0
col_count = 0

for i in range(N): # 행 탐색
    if 'X' not in castle[i]:
        row_count += 1

# list comprehension 활용하기 ★        
for j in range(M): # 열 탐색
    if 'X' not in [castle[i][j] for i in range(N)]:
        col_count += 1

print(max(row_count, col_count))