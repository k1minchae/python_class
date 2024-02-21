import math
# 내 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N + 1)]
    max_d = 0
    for y in range(N + 1):
        for x in range(N + 1):
            # 중계기 찾으면 그 뒤로 집의 좌표를 순회함
            if arr[y][x] == 2:
                for hy in range(N + 1):
                    for hx in range(N + 1):
                        if arr[hy][hx] == 1:
                            distance = (hy - y) ** 2 + (hx - x) ** 2
                            max_d = max(distance, max_d)

    result = math.ceil(math.sqrt(max_d))

    print(f'#{tc} {result}')


# 강사님 코드
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N + 1)]
    least_R = 0
    hi = hj = 0  # 중계기 좌표
    lst = []
    for i in range(N + 1):
        for j in range(N + 1):
            if area[i][j] == 1:
                lst.append([i, j])  # 집의 좌표

            if area[i][j] == 2:
                hi, hj = i, j

    for l in lst: # 집의 좌표 순회
        radius = ((l[0] - hi) ** 2 + (l[1] - hj) ** 2) ** 0.5  # 반지름
        least_R = max(radius, least_R)
        result = math.ceil(least_R)
    print(f'#{tc} {result}')