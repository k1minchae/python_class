N = int(input())
arr = [[i for i in range(N, 0, -1)], [], []]
result = 10 ** 6
temp = []
def DFS(start, cnt=0):
    global result
    if len(arr[2]) == N:
        if cnt < result:
            result = cnt
            print(temp)
        return temp
    if cnt > result:
        return
    if start == 2:
        return
    if arr[start]:
        s = arr[start].pop()
        for k in range(-1, 3):
            next = k + start
            if 0 < next <= 2 and next != start and (not arr[next] or s < arr[next][-1]):
                temp.append([start + 1, next + 1])
                arr[next].append(s)
                DFS(next, cnt + 1)
                arr[start].append(s)
                arr[next].pop()
                temp.pop()

print(DFS(0))

