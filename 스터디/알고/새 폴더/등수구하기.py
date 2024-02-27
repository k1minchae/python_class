# 1205 : 등수 구하기 (31120/40)
import sys
N, S, P = map(int, sys.stdin.readline().split())
rank = 1
cnt = 0 # 랭킹 인원수
if N != 0:
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)

    for score in arr:
        if score > S:
            rank += 1
            cnt += 1
        elif score == S:
            cnt += arr.count(S)
            break
        else:
            rank = cnt + 1
            break
    if cnt + 1 > P:
        rank = -1
    print(rank)

else:
    print(rank)

