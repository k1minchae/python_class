# 좋다
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
for tar in range(N):
    # 투포인터
    start = 0
    end = N - 1

    # 정상 범위 내에서만 계산
    while start < end:
        # 더했을때 목표값이 됨
        if arr[start] + arr[end] == arr[tar]:
            # 그게 자기 자신이 아니라면 cnt + 1
            if start != tar and end != tar:
                cnt += 1
                break
            # start 값이 자신이라면 + 1
            if start == tar:
                start += 1
            # end 값이 자신이라면 - 1
            if end == tar:
                end -= 1

        else: # 목표값 X -> 범위 좁히기
            if arr[start] + arr[end] > arr[tar]:
                end -= 1
            else:
                start += 1
print(cnt)
