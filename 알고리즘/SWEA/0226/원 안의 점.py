# 원 안의 점
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 반지름
    cnt = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if (i ** 2 + j ** 2) ** 0.5 <= N:
                cnt += 1
    print(f'#{tc} {cnt}')

# 강사님 코드

def get_count(N):
    cnt = 0
    for y in range(-N, N+1):
        for x in range(-N, N+1):
            ans = x ** 2 + y ** 2
            if ans <= N ** 2:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = get_count(N)
    print(f'#{tc} {result}')
