# 실버와 소수는 둘다 S로 시작한다
import sys

N = int(sys.stdin.readline())
arr = [1 for _ in range(N+1)]

b_cnt = 1
s_cnt = 0
last_B = True

for i in range(2, int(N**0.5)+1):
    if arr[i]:
        x = 2
        while x * i <= N:
            arr[x * i] = 0
            x += 1

for n in range(2, N+1):
    if arr[n]:
        if last_B:
            b_cnt -= 1
            s_cnt += 1
        s_cnt += 1
        last_B = False
    else:
        b_cnt += 1
        last_B = True
print(b_cnt, s_cnt)
