# 1로 만들기 (996 / 31120)
import sys
X = int(sys.stdin.readline())
min_cnt = float('inf')
def f(n, cnt = 0):
    global min_cnt
    if cnt > min_cnt:
        return
    if n == 1:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if n % 3 == 0:
        f(n//3, cnt + 1)
    if n % 2 == 0:
        f(n//2, cnt + 1)
    f(n-1, cnt + 1)
f(X)
print(min_cnt)