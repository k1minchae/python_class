T = int(input())

def f(s):
    global cnt
    n = C1[s]
    if n:
        cnt+=1
        f(n)
    n = C2[s]
    if n:
        cnt+=1
        f(n)

for tc in range(1, T+1):
    cnt = 1
    E, N = map(int, input().split())

    C1 = [0] * (E+2)
    C2 = [0] * (E+2)

    arr = list(map(int, input().split()))
    for i in range(0,len(arr),2):
        if not C1[arr[i]]:
            C1[arr[i]] = arr[i+1]
        else:
            C2[arr[i]] = arr[i+1]
    f(N)
    print(f'#{tc} {cnt}')