T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = [0] * (N+M+1)
    front = rear = -1

    for m in range(len(q)):
        rear += 1
        q[rear] = arr[(rear + 1) % (N) - 1]

    print(f'#{tc} {q[-1]}')
'''
# 덱으로 푸는 법
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 입력 받은 숫자들로 덱 생성
    arr = deque(map(int, input().split()))

    # for i in range(M):
    #     arr.append(arr.popleft())

    arr.rotate(-M)  # 원소들을 왼쪽으로 N 번 이동
    # M 이 양수면 오른쪽으로 N 번 이동

    result = arr[0]
    print(f'#{tc} {result}')
'''