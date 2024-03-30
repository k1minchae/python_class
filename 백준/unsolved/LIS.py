import sys
input = sys.stdin.readline
from bisect import bisect_left

T = int(input())
for tc in range(1, T+1):
    S = int(input())
    arr = [int(input()) for _ in range(S)]

        lis = []
        pos = [0] * S
        for i in range(S):
            idx = bisect_left(lis, arr[i])
            if idx >= len(lis):
                lis.append(arr[i])
            else:
                if lis[idx] != tar:
                    lis[idx] = arr[i]
            pos[i] = idx
        print(lis)
        ans = []
        len_ = len(lis) - 1
        for i in range(S-1, -1, -1):
            if pos[i] == len_:
                ans.append(arr[i])
                len_ -= 1
        print(ans)
        print('...')
    # print(f'Case #{tc}: {sum_}')
'''
input
1
3
3
1
2

output
[3]
[2, 1]
[2]
'''