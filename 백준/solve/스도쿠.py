import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(9)]

zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append([i, j])

def check(y, x, random):
    # 가로 검사
    for j in range(9):
        if j != x and arr[y][j] == random:
            return False

    # 세로 검사
    for i in range(9):
        if i != y and arr[i][x] == random:
            return False

    # 사각형 검사
    start_y, start_x = 3 * (y // 3), 3 * (x // 3)
    for i in range(start_y, start_y + 3):
        for j in range(start_x, start_x + 3):
            if i != y and j != x and arr[i][j] == random:
                return False

    return True

def solve(idx):
    if idx == len(zero):
        for row in arr:
            print(*row)
        # return
        sys.exit(0)

    y, x = zero[idx]
    for k in range(1, 10):
        if check(y, x, k):
            arr[y][x] = k
            solve(idx + 1)
            arr[y][x] = 0

solve(0)