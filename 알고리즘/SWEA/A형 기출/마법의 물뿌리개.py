# 마법의 물뿌리개
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = deque(sorted(list(map(int, input().split()))))
    target = arr.pop()   # 목표 나무의 크기
    day = 0
    done = False
    while done == False:
        if day % 2 == 0:
            water = 2
        else:
            water = 1
        while arr:
            tree = arr.popleft()
            if tree != target:
                day += 1
                if target - tree - water >= 0
                    tree += water

                    arr[tree] = arr[tree] - water
                    if arr[tree] == 0:

        else:
            water = 1
