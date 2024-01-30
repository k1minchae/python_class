import pprint
arr = [['_' for _ in range(5)] for _ in range(4)]

for _ in range(2):
    y, x = map(int, input().split())    # 폭탄 좌표
    
    # 폭탄 움직임 경우의 수
    dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]


    # 폭탄 위치
    for i in range(8):
        if (x + dx[i] >= 0) and  (x + dx[i] < 5) and (y + dy[i] >= 0) and (y + dy[i] < 4):
            bomb_x = x + dx[i]
            bomb_y = y + dy[i]
            arr[bomb_y][bomb_x] = '#'
    
for i in arr:
    print(*i)