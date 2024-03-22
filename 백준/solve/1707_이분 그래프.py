# 이분 그래프
from collections import deque
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    arr = [deque([]) for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)

    is_false = False
    check = [0] * V
    def f(s, mark):
        global is_false
        print(s, mark)
        if not check[s]:
            check[s] = mark
        if check[s] != mark:
            is_false = True
            return
        while arr[s]:
            n = arr[s].popleft()
            if not check[n]:
                f(n, mark)

    mark = 1
    for i in range(V):
        if not check[i]:
            f(0, mark)
            mark += 1
        if mark >= 3:
            is_false = True
            break

    if mark == 1:
        is_false = True
    print(check)
    if is_false:
        print('NO')
    else:
        print('YES')