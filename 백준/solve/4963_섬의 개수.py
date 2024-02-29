# 섬의 개수
import sys
input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    def island(y, x):
        if 0 > y or 0 > x or x >= w or y >= h:
            return
        if arr[y][x]:
            arr[y][x] = 0
            island(y-1, x)
            island(y+1, x)
            island(y, x + 1)
            island(y, x - 1)
            island(y-1, x-1)
            island(y+1, x-1)
            island(y-1, x+1)
            island(y+1, x+1)
            return True
        else:
            return False

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island(i, j):
                cnt += 1
    print(cnt)