# 컨테이너 운반
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 컨테이너 수 , 트럭 수
    s = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())))

    def container():
        cnt = 0
        while s and t:
            if t[-1] >= s[-1]:
                cnt += s[-1]
                t.pop()
            s.pop()
        return cnt
    print(f'#{tc}', container())