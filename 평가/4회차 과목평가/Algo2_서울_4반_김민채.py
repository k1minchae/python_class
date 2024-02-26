T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    y = x = 0
    is_end = False
    result = set()
    while is_end == False:
        ny = nx = 0
        max_val = 0     # M * M행렬 에서의 최댓값
        for i in range(y, y+M):
            for j in range(x, x+M):
                if 0 <= i < N and 0 <= j < N:
                    val = arr[i][j]
                    if val > max_val:
                        max_val = val
                        nx = j
                        ny = i
                    if i == j == (N-1):
                        is_end = True   # 끝까지 탐색했다면 종료
                        break
        result.add(max_val)
        if ny == y and nx == x: # 이전 최댓값과 같다면 종료
            break
        y = ny  # 다음에 탐색할 좌표
        x = nx
    print(f'#{tc} {sum(result)}')