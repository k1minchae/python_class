# N 과 M (9)
import sys

def f():
    if len(result) == M:
        print(*result)
        return

    before_num = 0
    for i in range(N):
        if not visited[i] and before_num != arr[i]:
            visited[i] = True
            result.append(arr[i])
            before_num = arr[i]

            f()
            visited[i] = False
            result.pop()


N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0] * N
result = []
f()