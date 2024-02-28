N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
start = arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] >= start:
        start = arr[i][1]
        cnt += 1
print(cnt)
