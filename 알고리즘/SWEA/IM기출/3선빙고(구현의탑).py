# # 3선 빙고 (구현의 탑)

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
