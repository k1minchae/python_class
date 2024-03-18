# 11729 : 하노이 탑 이동 순서
import sys
input = sys.stdin.readline
N = int(input())

# 최소 이동횟수는 공식으로 미리 구해두기
K = 2 ** N - 1

def f(n, start, end, middle):
    # 남은 원판이 하나일 때 start -> end 로 옮기기
    if n == 1:
        print(start, end)
        return

    # 남은 원판이 여러개일 때
    else:
        # n-1 개의 원판을 start -> middle 로 옮기기
        f(n-1, start, middle, end)

        # 가장 긴 n번쨰의 원판을 start -> end로 옮기기
        print(start, end)

        # middle로 옮겨둔 n-1개의 원판을 middle 에서 end 로 옮기기
        f(n-1, middle, end, start)
        return

print(K)
f(N, 1, 3, 2)