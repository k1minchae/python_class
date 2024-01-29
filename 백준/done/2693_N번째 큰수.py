import sys
T = int(input())
for _ in range(T):
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()
    print(A[-3])