# 레드 마운틴
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

def mountain(start):
    global result
    stack = []
    stack.append(start)

    while stack:
        x, y = stack.pop()

        if (x, y) == (n - 1, n - 1):
            result = 1
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0:
                stack.append((nx, ny))
                arr[ny][nx] = 1  # 방문한 곳은 다시 방문하지 않도록

mountain((0, 0))
print(result)