# 이진수2
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    cnt = -1
    result = []
    while N != 0.0:
        if len(result) > 12:
            result = ['overflow']
            break
        if N >= 2 ** cnt:
            N -= 2 ** cnt
            result.append(1)
        else:
            result.append(0)
        cnt -= 1
    print(f'#{tc} ', *result, sep='')
