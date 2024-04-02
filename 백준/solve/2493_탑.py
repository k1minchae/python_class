# 탑
import sys
input = sys.stdin.readline
N = int(input())  # 탑의 개수
arr = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > arr[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop() # 현재 값보다 작은 탑은 영원히 필요없음
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, arr[i]])  # 인덱스, 값

print(*answer)
