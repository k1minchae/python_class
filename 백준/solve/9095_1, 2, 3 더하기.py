# 1, 2, 3 더하기
import sys
input = sys.stdin.readline
T = int(input())
def plus(x):
    global cnt
    if x == n:
        cnt += 1
        return
    elif x > n:
        return
    return plus(x+1), plus(x+2), plus(x+3)
for _ in range(T):
    cnt = 0
    n = int(input())
    plus(0)
    print(cnt)