# 1459 : 걷기 (31120/40)
import sys
X, Y, W, S = map(int, sys.stdin.readline().split())

if 2 * W <= S: # 대각선이 손해
    print((X+Y) * W)

else:   # 가로 + 세로보다 대각선이 이득
    cross = min(X, Y)   # 최대한 대각선으로 갈 수 있는 정도
    not_cross = X + Y - 2 * cross  # 남은 직선거리

    if W > S:   # 한 칸보다 대각선이 이득
        print((not_cross // 2 * 2 + cross) * S + not_cross % 2 * W)
        # 남은 직선거리가 홀수일 때와 짝수일 때를 모두 만족시키기 위함

    else:   # 한 칸이 이득일 때
        print(cross * S + not_cross * W)