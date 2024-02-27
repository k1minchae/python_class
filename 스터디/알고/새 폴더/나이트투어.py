# 나이트 투어
import sys
D = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
start = sys.stdin.readline().rstrip() # 시작점

start_x = D[start[0]]
start_y = int(start[1]) - 1

before_x = start_x
before_y = start_y

visited = []
visited.append(start)

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, -1, 1, 1, -1]

result = 'Invalid'
for i in range(35):
    result = 'Invalid'
    S = sys.stdin.readline().rstrip()
    next_x = D[S[0]]
    next_y = int(S[1]) - 1

    for d in range(8):
        if 0 <= before_x + dx[d] < 6 and 0 <= before_y + dy[d] < 6:
            if before_x + dx[d] == next_x and before_y + dy[d] == next_y and S not in visited:
                result = 'Valid'
                before_y = next_y
                before_x = next_x
                visited.append(S)
                break

    if result == 'Invalid':
        break
if result == 'Valid':
    for j in range(8):
        if 0 <= before_x + dx[j] < 6 and 0 <= before_y + dy[j] < 6:
            if before_x + dx[j] == start_x and before_y + dy[j] == start_y:
                result = 'Valid'
                break
    else:
        result = 'Invalid'

print(result)