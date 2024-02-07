#카드 2
import sys
N = int(sys.stdin.readline())
arr = [i for i in range(1, N+1)]

for i in range(len(arr)):
    if len(arr) == 1:
        break
    arr.pop(0)
    arr.append(arr.pop(0))

print(*arr)
