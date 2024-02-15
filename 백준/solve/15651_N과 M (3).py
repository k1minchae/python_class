# N 과 M (3)
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = []
def f(level=0, temp = []):
    if level == M:
        result.append(temp)
        return
    for i in arr:
        temp.append(i)
        f(level+1, temp[:])
        temp.pop()

f()
for i in result:
    print(*i)