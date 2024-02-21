# Draw Tool
N = int(input())
Q = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(Q):
    c, y1, x1, y2, x2 = map(int, input().split())
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if c > arr[i][j]:
                arr[i][j] = c

def find_len(i, j):
    start = arr[i][j]  # 시작 위치의 색깔

    max_side = 0  # 최대 변의 길이
    for side in range(1, min(N - i, N - j) + 1): # 더 작은쪽으로 정사각형 길이 제한
        all_same_color = True
        for y in range(i, i + side):
            for x in range(j, j + side):
                if arr[y][x] != start:
                    all_same_color = False
                    break
            if not all_same_color:
                break
        if all_same_color:
            max_side = side

    return max_side ** 2

max_area = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:  # 색깔 발견
            area = find_len(i, j)
            max_area = max(max_area, area)

print(max_area)
