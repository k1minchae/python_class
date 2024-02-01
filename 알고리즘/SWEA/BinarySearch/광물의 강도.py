N, Q = map(int, input().split()) # N : 광물의 개수 // Q : 연구원의 수
arr = sorted(list(map(int, input().split()))) # 보유중인 광물의 강도
for _ in range(Q):
    S, E = map(int, input().split()) # 필요한 강도의 범위 (이상, 이하)
#
#     cnt = 0
#     for i in arr:
#         if S <= i <= E:
#             cnt += 1
#     print(cnt)
    start = 0
    end = max(arr)

    while start <= end:
        middle = (start + end) // 2
        cnt = 0
        for l in arr:
            cnt += l // middle
        if cnt
            if middle < S:
                start = middle + 1
            else:
                start