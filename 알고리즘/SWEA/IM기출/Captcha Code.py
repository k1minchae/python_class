T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split())) # N 개
    passcode = list(map(int, input().split())) # K 개

    finds = 0
    for i in range(N):
        if finds == K-1:
            break
        if sample[i] == passcode[finds]:
            finds += 1
    if finds == K-1:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')