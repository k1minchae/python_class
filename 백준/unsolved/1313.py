# 마법의 물뿌리개
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    def magic():
        day = 1
        target = max(arr)  # 목표 나무의 크기 (가장 큰 나무)
        if all(arr[i] == target for i in range(N)): return 0

        while True:
            if day % 2 == 0:  # 짝수 날
                water = 2  # 물을 주면 나무가 2만큼 자람
                for i in range(N):
                    tree = arr[i]
                    if tree + water <= target:
                        arr[i] += water
                        break

            else:  # 홀수 날
                water = 1  # 물을 주면 1만큼 자람
                for i in range(N):
                    tree = arr[i]
                    # 남은 길이가 홀수거나 3이상인 경우 물을 줌
                    if (target - tree) % 2 or (target - tree) >= 3:
                        arr[i] += water
                        break
                    # 남은 길이가 2 이상이면서 짝수인 경우가 더 있으면 물을 줌
                    elif target - tree and (target - tree) % 2 == 0:
                        cnt = 0
                        for x in range(N):
                            if target - arr[x] > 0 and (target - arr[x]) % 2 == 0:
                                cnt += 1
                        if cnt > 1:
                            arr[i] += water
                            break
            if all(arr[i] == target for i in range(N)): return day
            day += 1


    print(f'#{tc} {magic()}')