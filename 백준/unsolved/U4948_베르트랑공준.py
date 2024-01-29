# 자연수 n을 입력했을때, n~2n까지의 소수 개수 찾기
# n 보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.

'''시간초과 코드
import sys
N = int(sys.stdin.readline())
not_dec = [] # 소수가 아닌 것들을 담는 리스트
dec = []    # 소수인 것들 리스트

for i in range(N, 2 * N + 1):   # n 부터 2n까지 순회해서 소수 찾기
    for j in range(2, N):
        if i / j == i // j:
            not_dec.append(i)   # 소수가 아닌것에 추가
    if i not in not_dec:
        dec.append(i)

print(len(dec))
'''


# 풀다 맘...
import sys
A = []
B = []
row, col = map(int, sys.stdin.readline().split())

for i in range(row):
    i = list(map(int, sys.stdin.readline().split()))
    A.append(i)

for j in range(row):
    j = list(map(int, sys.stdin.readline().split()))
    B.append(j)

for k in range(row):
    for l in range(col):
        print(A[k][l] + B[k][l], end=' ')
    print()
