N, M = map(int, input().split()) # 세로, 가로
K = int(input()) # 화력

field = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    field[i] = list(input())
# 위에는 입력받는 코드

bomb_list = [] # 폭탄의 위치를 튜플로 저장 (세로,가로)

for i in range(N):
    for j in range(M):
        if field[i][j] == '@':
            bomb_list.append((i, j))

# 폭탄이 터뜨리는 범위
xbomb = []
ybomb = []

for i in range(-K, K+1):
