import heapq
T = int(input())
for tc in range(1, T + 1):
    lst = []
    N = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        heapq.heappush(lst, i)

    sum_v = 0
    def f(x):
        global sum_v
        if x == 0:
            return
        sum_v += lst[(x-1) // 2]
        f((x-1) // 2)

    f(N-1)
    print(f'#{tc} {sum_v}')
