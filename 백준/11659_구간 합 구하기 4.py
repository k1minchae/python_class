# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

x, y = map(int, input().split())
sum_v = sum(numbers[x-1:y])

for _ in range(M-1):
    i, j = map(int, input().split())
