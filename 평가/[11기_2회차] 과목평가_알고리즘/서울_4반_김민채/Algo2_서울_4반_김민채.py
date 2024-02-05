T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    curr = 0 # 개구리 시작 위치
    score = 0
    jump = arr[0]
    back_len = 0 # 직전에 뒤로 간 거리

    for k in range(K):
        if jump > 0:
            if back_len != 0: # 직젼에 뒤로갔다면
                jump = arr[curr] - back_len # 직전에 뒤로간만큼 앞으로 
                if curr + jump > len(arr) - 1: # 연못에 빠짐
                    break
                else:
                    curr += jump
                    jump = arr[curr]
                    score += arr[curr]
                    back_len = 0 # 초기화
            else: # 직전에 뒤로가지 않았다면
                if curr + jump > len(arr) - 1:
                    break
                else:
                    curr += jump
                    score += arr[curr]
                    jump = arr[curr]

        else:
            if curr + jump < 0: # 연못에 빠지는 경우
                break
            else:
                curr += jump
                back_len = jump
                jump = arr[curr]
                score += arr[curr]

    print(f'#{tc} {score}')

# 강사님 코드
def jump(data):
    score = 0 # 점수
    prev = 0 # 이전 점프 거리
    pos = 0 # 현재 위치

    for _ in range(M):
        next = data[pos] # 다음에 점프할 거리
        if data[pos] > 0 and prev < 0: # 만약 이전에 뒤로 점프했다면
            next += -prev
        prev = data[pos] # 현재 점프 거리 저장
        pos += next # 점프
        if pos < 0 or pos >= N:  # 위치를 벗어나면
            return score
        score += data[pos]
    return score

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int(input().split()))
    data = list(map(int, input().split()))
    result = jump(data)

    print(f'#{tc} {result}')