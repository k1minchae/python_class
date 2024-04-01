# 로봇 프로젝트
import sys
input = sys.stdin.readline
try:
    while True:
        x = int(input()) # 구멍 너비
        x *= 10 ** 7 # cm -> nm 변환
        n = int(input()) # 레고 개수
        lego = [int(input()) for _ in range(n)] # 각 레고의 길이 저장
        lego.sort()

        start = 0
        end = n-1
        while start <= end:
            val = lego[start] + lego[end]
            # 값 찾았다면 종료
            if val == x and start != end:
                print('yes', lego[start], lego[end])
                break
            elif val > x:
                end -= 1
            else:
                start += 1
        else: # 반복문이 break 되지 않았다면 못찾은거 -> danger출력
            print('danger')
except:
    exit()