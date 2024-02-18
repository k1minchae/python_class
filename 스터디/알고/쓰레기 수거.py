# 쓰레기 수거
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    W, N = map(int, input().split()) # 용량, 노드개수
    curr = cnt = 0
    trash = W
    for n in range(N):
        x_i, w_i = map(int, input().split()) # 다음 쓰레기장 거리, 쓰레기 양
        cnt += x_i - curr
        curr = x_i
        trash -= w_i
        if trash < 0: # 쓰레기 처리 불가능
            cnt += x_i * 2  # 비우고 다시 옴
            trash = W - w_i
        elif not trash:
            cnt += x_i # 쓰레기 비우러 감
            trash = W
            curr = 0
    cnt += curr # 처리 끝
    print(cnt)