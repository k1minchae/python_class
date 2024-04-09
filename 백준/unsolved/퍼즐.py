import sys
from heapq import heappop, heappush
input = sys.stdin.readline
puzzle = [list(input().split()) for _ in range(3)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 퍼즐이 다 맞추어진 문자열
done = '123456780'

s = '' # 초기 arr상태를 저장할 문자열
sy, sx = 0, 0 # 처음 0이 시작되는 좌표
for i in range(3):
    for j in range(3):
        s += puzzle[i][j]
        if puzzle[i][j] == '0':
            sy = i
            sx = j

q = [(0, s, sy, sx)] # 초기상태 q에 저장해둠
def f():
    # 퍼즐을 움직일때마다 퍼즐 상태와 이동횟수를 저장할 dict
    result = {}
    result[s] = 0 # 처음 상태의 이동횟수는 0
    while q:
        cost, st, y, x = heappop(q) # 이동횟수, 퍼즐상태 문자열, 좌표
        # 퍼즐이 다 완성되었다면
        if st == done:
            # 이동횟수 출력
            print(result[done])
            return
        # 더 적은횟수로 현재 상태에 도달한 적이 있다면 continue
        # 도달한적이 없다면 무한대값과 비교해서 continue되지 않도록 함
        if result.get(st, float('inf')) < cost:
            continue
        for dy, dx in dir: # 다음좌표 찾기
            ny, nx = y + dy, x + dx
            if 0 <= ny < 3 and 0 <= nx < 3: # 범위 안에서만 바꾸기
                tar_idx = ny * 3 + nx # 바꾸려고 하는 숫자의 인덱스
                tar = st[tar_idx] # 바꾸려는 문자
                temp = st.replace('0', '9') # 0을 잠시 9로 바꿔둠
                nst = temp.replace(tar, '0') # 바꾸려는 숫자를 0으로 바꿈
                new = nst.replace('9', tar) # 0를 바꾸려는 숫자로 바꿔줌

                # 다음 값에 더 적은 횟수로 도달한 적이 있다면 continue
                if result.get(new, float('inf')) <= cost + 1:
                    continue
                # continue 되지 않았다면 q에 다음 값 추가, 결과에 저장
                heappush(q, (cost + 1, new, ny, nx))
                result[new] = cost + 1
    # 모든 경우의수 다해봐도 퍼즐이 완성되지 않는다면 -1
    print(-1)
f() # 함수호출