# N과 M (5)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
def btc(level= 0, temp = []):
    if level == M:
        if temp not in result:
            result.append(sorted(temp[:]))
        return
    for i in arr:
        temp.append(i)
        btc(level + 1, temp[:])
        temp.pop()
btc()
result.sort()
for i in result:
    print(*i)