# 작년 IM 기출
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    word_count = 0
    # 가로 칸 탐색
    for i in range(N):
        for j in range(N):
            if (j+K <= N) and (arr[i][j] == 1):
                cnt = 1
                for k in range(1, N-j+1): # 선택 칸 기준 맨 끝까지 탐색
                    if ((j + k) < N) and (arr[i][j+k]) == 1: # 범위 안에서 1발견하면 cnt
                        cnt += 1
                    if ((j + k) < N) and arr[i][j+k] == 0: # 0 발견하면 break
                        break
                if cnt == K:  # 카운트가 K랑 일치하면 (커도 안 됨)
                    if (j-1 >= 0) and arr[i][j-1] == 0: # 이전 칸이 막혀있을 때
                        word_count += 1  # 정확한 단어 count
                    elif j == 0:  # 이전칸이 없을 경우도
                        word_count += 1  # 정확한 단어 count

    # 세로 탐색 -> 가로랑 똑같음
    for j in range(N):
        for i in range(N):
            if (i+K <= N) and (arr[i][j] == 1):
                cnt = 1
                for k in range(1, N-i+1):
                    if ((i + k) < N) and (arr[i+k][j]) == 1:
                        cnt += 1
                    if ((i + k) < N) and arr[i+k][j] == 0:
                        break
                if cnt == K:
                    if (i-1 >= 0) and arr[i-1][j] == 0:
                        word_count += 1
                    elif i == 0:
                        word_count += 1
    print(f'#{tc} {word_count}')


'''라이브 강사님 코드
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    # 오른쪽과 아래쪽에 0으로된 줄 추가
    arr = [list(map(int, input().split())+ [0]) for _ in range(N) = [[0] * (N+1)]] 
    N += 1   # 줄 추가해서 N 이 하나 커짐
    
    word_count = 0
    
    # 가로 탐색
    for i in range(N):  # i 행에서 연속한 1의 개수 카운트
        cnt = 0     
        for j in range(N):  
            if arr[i][j]:  # 1이면
                cnt += 1
            else:    # arr[i][j] == 0 이면
                if cnt == K: 
                    world_count += 1
                cnt = 0
            
    # 세로 탐색
    # 은 귀찮아서 안적음 (똑같이 하면 됨)
'''