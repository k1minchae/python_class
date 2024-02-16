# 2422 : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
dont_mix = [list(map(int, input().split())) for _ in range(M)]
ice_cream = [i for i in range(1, N+1)]
cnt = 0
