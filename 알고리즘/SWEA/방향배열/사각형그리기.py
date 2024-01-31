T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for start_i in range(N):
        for start_j in range(N):
            for end_i in range(N):
                for end_j in range(N):
                    if arr[end_i][end_j] == arr[start_i][start_j]: # 2번 조건 충족
                        if end_i >= start_i and end_j >= start_j: # 1번 조건 충족
                            result.append((end_i - start_i + 1) * (end_j - start_j + 1)) # 면적값
    print(f'#{tc} {result.count(max(result))}') # 면적값 중에서 최대값의 개수를 센다.