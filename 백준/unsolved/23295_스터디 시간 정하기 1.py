# 스터디 시간 정하기 1
import sys
input = sys.stdin.readline
N, T = map(int, input().split())
arr = [[]for _ in range(N)]
start = 0
end = start + T

fin = 0
for n in range(N):
    I = int(input())
    for _ in range(I):
        a, b = map(int, input().split())
        arr[n].append((a, b))
        fin = max(b, fin)

# 초기값
pre_t = 0
for n in range(N):
    for s, e in arr[n]:
        if s >= end:
            continue
        pre_t += min(e, end) - max(s, start)

max_t = 0
result_s = 0
result_e = 0
while end <= fin:
    t = pre_t
    for n in range(N):
        for s, e in arr[n]:
            if s <= start and e > start:
                t -= 1
            if end+1 <= e and s < end:
                t += 1
    start += 1
    end += 1
    if t > max_t:
        max_t = t
        result_s = start
        result_e = end
    pre_t = t

print(result_s, result_e)