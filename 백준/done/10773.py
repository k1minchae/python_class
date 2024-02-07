import sys
K = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(K)]
result = []
for i in arr:
    if i == 0:
        result.pop()
    else:
        result.append(i)
print(sum(result))