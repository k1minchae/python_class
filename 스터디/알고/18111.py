# 마인크래프트
import sys
N, M, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_t = float('inf')
ground = 0
for std in range(257): # 표준 땅
    rm_g = 0    # 땅 제거
    ad_g = 0    # 땅 추가
    for y in range(N):
        for x in range(M):
            if arr[y][x] > std: # 제거
                rm_g += arr[y][x] - std
            else:   # 추가
                ad_g += std - arr[y][x]
    inv = B + rm_g
    if inv < ad_g:  # 인벤 부족
        continue
    time = rm_g * 2 + ad_g
    if time <= min_t:
        min_t = time
        ground = std
print(min_t, ground)