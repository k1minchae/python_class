# 최애의 팀원
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    name, code = input().split()
    q.append([name, int(code)])

def team():
    while len(q) > 2:
        cnt = 0
        X, num = q.popleft()
        while True:
            cnt += 1
            is_team = q.popleft()
            if cnt != num: # 팀원 못찾음
                q.append(is_team)   # 다시 큐에 넣기
            if cnt == num:
                break
    print(q[0][0])  # 마지막 남은 사람 출력
    return

team()