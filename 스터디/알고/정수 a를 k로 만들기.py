# 정수 a를 k로 만들기
import sys
input = sys.stdin.readline
A, K = map(int, input().split())
min_cnt = float('inf')
def f(a,cnt = 0):
    global min_cnt
    if a > K or cnt > min_cnt:
        return
    if a == K:
        min_cnt = min(min_cnt, cnt)
        return
    f(a+1, cnt+1)
    f(a*2, cnt+1)

f(A)
print(min_cnt)