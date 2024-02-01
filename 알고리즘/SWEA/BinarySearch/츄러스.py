N, K = map(int, input().split()) # N : 츄러스 개수, K : 요청 분할 개수
arr = []
for _ in range(N):
    arrs = int(input())
    arr.append(arrs)
arr.sort(reverse=True)

while len(arr) < K:
    arr.append(arr.pop(0) // 2)
    arr.append(arr[-1])
    arr.sort(reverse=True)

if K ==1:
    print(max(arr))

for i in range(1, len(arr)+1):
    while arr[-i] < (arr[i-1] // 2):
        arr[i-1] = (arr[i-1] // 2)
        arr.append(arr[i-1] // 2)
        arr.sort(reverse=True)
print(min(arr[:K-1]))


# ??