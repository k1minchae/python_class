# 욕심쟁이 판다
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DP = [[-1] * n for _ in range(n)]  # DP 배열 -1로 초기화

def DFS(sy, sx):
    if DP[sy][sx] != -1:  # 이미 계산된 경우 그 값을 반환
        return DP[sy][sx]

    eat = arr[sy][sx]
    max_cnt = 1  # 초기 칸 수 포함
    for dy, dx in dirs:
        ny = dy + sy
        nx = dx + sx
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > eat:
            max_cnt = (max_cnt, 1 + DFS(ny, nx))  # 재귀 돌려서 최대 대나무 개수 구함
    DP[sy][sx] = max_cnt  # 계산된 값 DP에 저장
    return max_cnt

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, DFS(i, j))

print(result)
