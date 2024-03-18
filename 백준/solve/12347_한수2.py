import heapq
import sys
N = int(sys.stdin.readline())

if N < 100:
    print(N)
else:
    if N < 111:
        print(99)
    else:
        cnt = 99
        q = [i for i in range(11, 100)]

        while True:
            x = heapq.heappop(q)
            ten = x // 10 % 10
            one = x % 10

            next_one = one * 2 - ten
            if 0 <= next_one < 10:
                nx = x * 10 + next_one
                if nx > N:
                    print(cnt)
                    break
                heapq.heappush(q, nx)
                cnt += 1
