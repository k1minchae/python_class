# 2차원 배열
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
# 위에는 입력받는 코드

dx = [] # 마법사의 x축 공격방향 저장
dy = []

for i in range(-K, K+1):
    if i == 0:
        continue
    dx.append(i)
    dy.append(i) # 여기까지하면 3사분면, 1사분면만 됨

dy.extend(dy)
dx.extend((reversed(dx))) # 공격범위에 2사분면과 4사분면도 추가

kill_list = [] # 죽인 몬스터의 모든 경우의수 저장
for i in range(N):
    for j in range(N):
        monster = 0
        for k in range(4 * K): # 공격의 모든 경우의 수
            # 범위 벗어날 경우 continue
            if (i+dy[k]) < 0 or (i + dy[k]) > (N-1) or (j+dx[k]) < 0 or (j+dx[k]) > (N-1):
                continue
            else:
                monster += field[i+dy[k]][j+dx[k]]
        kill_list.append(monster)

print(max(kill_list)) # 몬스터 죽인 수 중에서 최대값 출력
