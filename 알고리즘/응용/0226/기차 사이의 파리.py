# 기차 사이의 파리
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    t = D / (A+B)
    fly_d = F * t

    print(f'#{tc} {fly_d:.10f}')

'''
T = 250 / (A+B) * F
나눗셈을 먼저 하면 오차 발생
오차에 F를 곱하면 오차가 더욱 커진다.
T = 250 * F / (A+B) 처럼 F 를 먼저 곱하고 (A+B)를 나누면 더 정확한 값이 계산된다
'''
# 강사님 코드
testcase = int(input())
for tc in range(1, testcase+1):
    D, A, B, F = map(int, input().split())

    T = D * F / (A + B)
    print(f'#{tc} {T}')