T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 오른쪽과 아래쪽에 0으로된 줄 추가
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

    N += 1
    world_count = 0
    for i in range(N): # 가로
        cnt = 0
        for j in range(N):
            if arr[i][j]: # 빈 칸일때
                cnt += 1
            else:
                if cnt == K:
                    world_count += 1
                cnt = 0 # 초기화

    for j in range(N): # 세로
        cnt = 0
        for i in range(N):
            if arr[i][j]: # 빈 칸일때
                cnt += 1
            else: # 검은 칸을 만나면
                if cnt == K: # 판별하기
                    world_count += 1
                cnt = 0 # 초기화

    print(f'#{tc} {world_count}')