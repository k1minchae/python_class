# KMP 알고리즘
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
x = 'IO' * N + 'I'
len_x = len(x)

i = 0
cnt = 0
temp = S[:len_x]
while len_x+i < M:
    if temp == x:
        cnt += 1
    temp = temp[1:] + S[len_x+i]
    i += 1

print(cnt)
