# 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]

for _ in range(M):
    numbers = '0123456789'
    Q = sys.stdin.readline().rstrip()
    if Q[0] in numbers:
        print(arr[int(Q) - 1])
    else:
        print(arr.index(Q) + 1)
