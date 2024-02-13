# 좋은 구간
import sys
L = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
if n in arr:
    result = 0
else:
    arr.append(n)
    arr.sort()
    n_idx = arr.index(n)
    if n_idx == 0:
        a = n
        b = arr[1] - n
    else:
        a = n - (arr[n_idx - 1])
        b = arr[n_idx + 1] -n
    result = a * b -1
print(result)