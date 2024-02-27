# 산타소년단
N = int(input())

cnt = 0
visited = [0] * 5
temp = []
def f(x):
    global cnt
    if x == N:
        if 0 in temp:
            cnt += 1
        return
    for i in range(5):
        if not visited[i]:
            temp.append(i)
            visited[i] = 1
            f(x+1)
            visited[i] = 0
            temp.pop()
f(0)

print(cnt)
