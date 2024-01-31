N, M = map(int, input().split())  # 세로, 가로
K = int(input())  # 화력


def bomb(N, M, K, arr):


        arr = [list(input()) for _ in range(N)]  # 주어진 맵
        # 위에는 입력받는 코드


        bomb_list = []  # 폭탄의 위치를 튜플로 저장 (세로,가로)
        for i in range(N):
            for j in range(M):
                if arr[i][j] == '@':
                    bomb_list.append([i, j])


        # 폭탄이 터지는 방향
        xbomb = [0, 0, -1, 1, 0]  # 상 하 좌 우 중앙
        ybomb = [1, -1, 0, 0, 0]

        # 터뜨리기
        for i in range(5):
            for j in range(1, K + 1):
                for y, x in bomb_list:
                    ny = y + ybomb[i] * j
                    nx = x + xbomb[i] * j
                    if nx >= 0 and nx < M and ny >= 0 and ny < N:
                        if arr[ny][nx] == '#':
                            break
                        arr[ny][nx] = '%'
        return arr

result = bomb(N, M, K)
print(result)

