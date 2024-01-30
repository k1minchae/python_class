N, M = map(int, input().split()) # 세로, 가로
K = int(input()) # 화력

field = [list(input()) for _ in range(N)] # 주어진 맵
# 위에는 입력받는 코드

bomb_list = [] # 폭탄의 위치를 튜플로 저장 (세로,가로)
for i in range(N):
    for j in range(M):
        if field[i][j] == '@':
            bomb_list.append((i, j))

# 폭탄이 터지는 길이와 방향
xbomb = []
ybomb = [] # 경우의수 : (2 * K + 1) * 2
for i in range(-K, K+1):
    xbomb.append(i)
    ybomb.append(0)
ybomb.extend(xbomb)
xbomb.extend(ybomb[0:2 * K + 1])

wall_list = [] # 벽 인덱스를 (y, x) 형태로 저장
# 벽 인덱스 구하기
for i in range(N):
    for j in range(M):
        if field[i][j] == '#':
            wall_list.append((i, j))

# 실제 폭탄이 터지는 index

for wally, wallx in wall_list:
    for bomby, bombx in bomb_list: # bomby, bombx = 폭탄의 위치
        for i in range(len(xbomb)):
            if ((xbomb[i] + bombx) < 0) or ((xbomb[i]+bombx) >= M) or ((ybomb[i]+bomby) < 0) or ((ybomb[i]+bomby) >= N):
                continue # 폭탄 터지는게 필드 밖으로 벗어나면 continue

            else:
                field[(ybomb[i]+bomby)][(xbomb[i]+bombx)] = '%'



for i in field:
    print(''.join(i))