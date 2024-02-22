import heapq
Q = int(input())
arr = list(map(int, input().split()))
temp = [1]
result = []
heapq.heappush(temp, 2)
heapq.heappush(temp, 3)
heapq.heappush(temp, 5)

while len(result) != max(arr):
    var = heapq.heappop(temp)
    if var not in temp:
        result.append(var)
        heapq.heappush(temp, var * 2)
        heapq.heappush(temp, var * 3)
        heapq.heappush(temp, var * 5)

for k in arr:
    print(result[k-1], end = ' ')

