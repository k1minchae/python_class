import copy
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr2 = copy.deepcopy(arr)
    result_list = [0] * 10
    for a in range(0, 5):
        for i in range(N-1):
            max_idx = i
            for j in range(i+1, N):
                if arr[j] > arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        result_list[2 * a] = arr[a]

    for a in range(0, 5):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if arr2[j] < arr2[min_idx]:
                    min_idx = j
            arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
        result_list[2 * a + 1] = arr2[a]

    print(f'#{tc}', end= ' ')
    print(*result_list)
