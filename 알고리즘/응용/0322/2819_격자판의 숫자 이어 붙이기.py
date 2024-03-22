# 2819. 격자판의 숫자 이어 붙이기
def dfs(y, x, temp='', level = 0):
    num = str(arr[y][x])
    if level == 7:
        result.add(temp)
        return
    for dy, dx in dir:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, temp + num, level + 1)

T = int(input())
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j)
    print(f'#{tc} {len(result)}')