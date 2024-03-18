def f(start, end, target, pos = ''):
    global cnt
    mid = (start + end) // 2

    if start > end: # 기저조건
        return

    if A[mid] == target:    # 기저조건 2
        cnt += 1
        return

    else:
        if target < A[mid]:
            if pos == 'L':
                return
            else:
                f(start, mid-1, target, 'L')
        else:
            if pos == 'R':
                return
            else:
                f(mid+1, end, target, 'R')
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for b in B:
        f(0, N-1, b)
    print(f'#{tc} {cnt}')