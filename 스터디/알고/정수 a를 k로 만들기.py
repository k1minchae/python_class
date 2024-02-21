# 정수 a를 k로 만들기
import sys
input = sys.stdin.readline
A, K = map(int, input().split())
cnt = 0

while True:
    if A == K:
        break
    if K % 2 == 0 and K // 2 >= A:
        K //= 2
    else:
        K -= 1
    cnt += 1

print(cnt)