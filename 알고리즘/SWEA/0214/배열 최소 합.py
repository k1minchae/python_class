def f(row, sum=0):
    global min_sum
    if sum >= min_sum:
        return
    if row == N and sum < min_sum:
        min_sum = sum
        return
    for col in range(N):
        if col not in visited:
            visited.append(col)
            f(row+1, sum + arr[row][col])
            visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    visited = []
    f(0)
    print(f'#{tc} {min_sum}')