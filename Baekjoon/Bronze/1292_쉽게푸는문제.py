import sys
A, B = map(int, sys.stdin.readline().split())

list = []
for i in range(1, B + 1):
    if list.count(i) < i:
        for j in range(0, i):
            list.append(i)

print(sum(list[(A - 1) : (B)]))