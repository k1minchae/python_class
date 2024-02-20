# 개미
import sys
input = sys.stdin.readline
w, h = map(int, input().split())
p, q = map(int, input().split())    # 초기 위치 x , y
t = int(input())    # 움직일 시간

# 0, 0 기준 움직일 거리를 왕복 최대 거리로 나눈 나머지
nx = (t + p) % (2 * w)
ny = (t + q) % (2 * h)

if nx > w:
    nx = 2 * w - nx

if ny > h:
    ny = 2 * h - ny

print(nx, ny)