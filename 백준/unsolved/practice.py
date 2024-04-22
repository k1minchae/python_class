# 수 나누기 게임
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
idx = [i for i in range(0, N)]
score = [0] * N

temp = [[] for _ in range(max_num+1)]
for i in range(N):
    for j in range(arr[i], max_num+1, arr[i]):
        temp[j].append(i)

for i in range(N):
    for idx in temp[arr[i]]:
        if idx != i:
            score[idx] += 1
            score[i] -= 1
print(*score)