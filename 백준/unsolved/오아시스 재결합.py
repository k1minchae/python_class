# 거짓말
N, M = map(int, input().split())
T, *arr = map(int, input().split()) # 진실아는 사람수, 번호
parents = [i for i in range(N+1)]

if T == 0:
    print(M)
    exit(0)

else:
    arr = set(arr)
    parties = []
    cnt = 0
    for _ in range(M):
        n, *lst = map(int, input().split())
        if set(lst) & arr:
            arr = set.union(arr, set(lst))
        parties.append(lst)

    for party in parties:
        arr = set.union(set(party), arr)

    for party in parties:
        if set(party) & arr:
            arr=set.union(arr, set(party))
            continue
        cnt += 1
    print(cnt)
    # print(arr)
