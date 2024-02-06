import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N + 1)]
    dist_list = []  # 중계기랑 가장 멀리 떨어진 집을 찾기 위한 list
    for y in range(N + 1):
        for x in range(N + 1):

            if arr[y][x] == 2:  # 중계기 찾으면 그 뒤로 집의 좌표를 순회함
                for hy in range(N + 1):
                    for hx in range(N + 1):
                        if arr[hy][hx] == 1:
                            dist_list.append((hy - y) ** 2 + (hx - x) ** 2)
    max_d = max(dist_list)

    result = math.ceil(math.sqrt(max_d))

    print(f'#{tc} {result}')
