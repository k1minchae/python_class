N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
# for i in range(N-1):
#     for j in range(i+1, N):
#         if arr[i][1] > arr[j][1]:
#             arr[i], arr[j] = arr[j], arr[i]
#         elif arr[i][1] == arr[j][1]:
#             if arr[i][0] > arr[j][0]:
#                 arr[i], arr[j] = arr[j], arr[i]

cnt = 1
start = arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] >= start:
        start = arr[i][1]
        cnt += 1
print(cnt)
