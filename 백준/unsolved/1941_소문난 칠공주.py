# 소문난 칠공주
import sys
from collections import deque
arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]

# 가로, 세로 인접 여부 체크
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상 하 좌 우
result = []
visited = [[0] * 5 for _ in range(5)]
def BFS(sy, sx):
    global result

    # q와 visited 설정하고 시작
    q = deque([])
    if arr[sy][sx] == 'Y':

        q.append([sy, sx, 0, 1, {(sy, sx)}])  # y, x, S, Y, cnt
    else:
        q.append([sy, sx, 1, 0, {(sy, sx)}])
    visited[sy][sx] = 1

    while q:
        y, x, S, Y, cnt = q.popleft()
        if len(cnt) == 7:
            print('cnt', cnt)
            if cnt not in result:
                result.append(cnt)
                print('result', result)
        else:
            for dy, dx in dir:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                    if arr[ny][nx] == 'Y':
                        if Y+1 > 3: # 임도연파가 우위를 점한경우
                            continue
                        else:
                            visited[ny][nx] = 1
                            cnt.add((ny, nx))
                            q.append([sy, sx, S, Y+1, cnt])

                    else:   # 이다솜파
                        visited[ny][nx] = 1
                        cnt.add((ny, nx))
                        q.append([sy, sx, S+1, Y, cnt])

for i in range(5):
    for j in range(5):
        BFS(i, j)
print(len(result))
