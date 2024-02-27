# 6615 : 콜라츠 추측
import sys
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    A = a
    B = b
    visited = {}
    visited[a] = 0
    while True:
        if a == 1:
            break
        if a % 2 == 0:
            next = a // 2
        else:
            next = a * 3 + 1
        visited[next] = visited.get(a) + 1
        a = next

    b_cnt = 0
    while True:
        if visited.get(b) != None:
            a_cnt = visited[b]
            c = b
            break
        if b % 2 == 0:
            b = b // 2
        else:
            b = b * 3 + 1
        b_cnt += 1

    print(f"{A} needs {a_cnt} steps, {B} needs {b_cnt} steps, they meet at {c}")
