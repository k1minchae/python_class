#카드 2
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = deque([i for i in range(1, N+1)])

for i in range(len(arr)):
    if len(arr) == 1:
        break
    arr.popleft()
    arr.append(arr.popleft())

print(*arr)
