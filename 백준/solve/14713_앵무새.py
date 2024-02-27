# 앵무새
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [deque(list(sys.stdin.readline().split())) for _ in range(N)]
L = deque(list(sys.stdin.readline().split()))

def bird():
    while L:
        delete = False
        for n in range(N):
            if not arr[n]:
                continue
            if arr[n][0] == L[0]:
                L.popleft()
                arr[n].popleft()
                delete = True
                break
        if not delete:
            return 'Impossible'
    for n in range(N):
        if arr[n]:
            return 'Impossible'
    return 'Possible'

print(bird())