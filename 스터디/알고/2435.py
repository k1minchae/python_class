N, K = map(int, input().split())
arr = list(map(int, input().split()))
K_list_sum = []

if K == 1:
    print(max(arr))

elif N == K:
    print(sum(arr))

else:
    for i in range(N-K+1):
        K_list_sum.append(sum(arr[i:i+K]))

    print(max(K_list_sum))