T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 ** 6

    def f(product, cost, visited):
        global result
        if product == N - 1:
            result = min(result, cost)  # 최소값 업데이트
            return
        if cost >= result:  # 가지치기
            return
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                f(product + 1, cost + arr[product + 1][i], visited)
                visited[i] = 0  # 방문표시 되돌리기


    for j in range(N):
        visited = [0] * N
        visited[j] = 1
        f(0, arr[0][j], visited)

    print(f'#{tc} {result}')