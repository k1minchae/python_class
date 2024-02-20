# # 3선 빙고 (구현의 탑)
#
# MAP = [list(map(int, input().split())) for _ in range(5)]
# num = []
# for _ in range(5):
#     num.extend(list(map(int, input().split())))
#
# bingo = 0
# def find(y, x):
#     global bingo
#     if MAP[y].count(0) == 4: # 가로
#         bingo += 1
#
#     cnt_v = 0
#     for k in range(5): # 세로
#         if MAP[k][x] == 0:
#             cnt_v += 1
#     if cnt_v == 4:
#         bingo += 1
#
#     cnt_c = 0
#     for k in range(-2, 3):  # 대각
#         if 0 <= y+k < 5 and 0 <= x+k < 5 and MAP[y+k][x+k] == 0:
#             cnt_c += 1
#     if cnt_c == 4:
#         bingo += 1
#
#     if bingo >= 3:   # 3빙고 되면
#         return True
#
# def game():
#     for n in num:
#         for y in range(5):
#             for x in range(5):
#                 if MAP[y][x] == n:
#                     if find(y,x):
#                         return n
#                     MAP[y][x] = 0
# print(game())
MAP = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num.extend(list(map(int, input().split())))

def find_bingo():
    bingo_count = 0

    # 가로, 세로 빙고 확인
    for i in range(5):
        if all(MAP[i][j] == 0 for j in range(5)):  # 가로 빙고 확인
            bingo_count += 1
        if all(MAP[j][i] == 0 for j in range(5)):  # 세로 빙고 확인
            bingo_count += 1

    # 대각선 빙고 확인
    if all(MAP[i][i] == 0 for i in range(5)):  # 왼쪽 위에서 오른쪽 아래로 대각선
        bingo_count += 1
    if all(MAP[i][4 - i] == 0 for i in range(5)):  # 오른쪽 위에서 왼쪽 아래로 대각선
        bingo_count += 1

    return bingo_count

def game():
    for n in num:
        for i in range(5):
            for j in range(5):
                if MAP[i][j] == n:
                    MAP[i][j] = 0
                    if find_bingo() >= 3:
                        return n

print(game())
