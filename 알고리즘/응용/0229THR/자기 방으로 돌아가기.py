# 자기 방으로 돌아가기
'''
5 -> 7 이나 7 -> 5나 결과가 같다
아랫방을 모두 윗방으로 이주하더라도 결과는 같음
만약 짝수라면 s -=1 e-= 1 해서 윗방으로 올리자
'''
T = int(input())
cnt = 0
for tc in range(1, T+1):
    N = int(input())    # 학생 수
    arr = [0] * 401    # 복도 리스트
    for _ in range(N):
        a, b = map(int, input().split())
        if a % 2 == 0:
            a -= 1
        if b % 2 == 0:
            b -= 1
        s = min(a, b)   # 시작 방
        e = max(a, b)   # 끝 방

        for i in range(s, e + 1):
            arr[i] += 1

    print(f'#{tc} {max(arr)}')