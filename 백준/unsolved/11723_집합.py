# 집합
import sys
S = set()
M = int(sys.stdin.readline())
for _ in range(M):
    C = list(sys.stdin.readline().split())
    if C[0] == 'add':
        S.add(C[1])
    elif C[0] == 'check':
        if C[1] in S:
            print(1)
        else:
            print(0)
    elif C[0] == 'remove':
        if C[1] in S:
            S.remove(C[1])
    elif C[0] == 'toggle':
        if C[1] in S:
            S.remove(C[1])
        else:
            S.add(C[1])
    elif C[0] == 'all':
        S = set(str(i) for i in range(1, 21))
    elif C[0] == 'empty':
        S.clear()
