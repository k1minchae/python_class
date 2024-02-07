# 나이순 정렬
import sys

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip().split()) + [i] for i in range(N)]

arr.sort(key=lambda x: (int(x[0]), x[2]))
for i in arr:
    print(*i[:2])
