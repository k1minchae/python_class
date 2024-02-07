T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for start_i in range(N):
        for start_j in range(N): # 시작 좌표 고정 (j, i)
            for end_i in range(N):
                for end_j in range(N): # 끝 좌표 순회
                    if arr[end_i][end_j] == arr[start_i][start_j]: # 숫자가 같음
                        if end_i >= start_i and end_j >= start_j: # 끝좌표가 더 큼
                            result.append((end_i - start_i + 1) * (end_j - start_j + 1)) # 면적
    print(f'#{tc} {result.count(max(result))}') # 최대값의 면적 count