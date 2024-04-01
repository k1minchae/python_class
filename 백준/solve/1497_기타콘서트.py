# 기타콘서트
def DFS(x, temp, s_cnt = 0, g_cnt = 1):
    global max_cnt, guitar
    G, S = arr[x]  # 기타와 연주할 수 있는 노래
    for m in range(M):
        if not temp[m] and S[m]:
            temp[m] = 1
            s_cnt += 1

    if s_cnt > max_cnt:
        max_cnt = s_cnt
        guitar = g_cnt

    elif s_cnt == max_cnt and s_cnt != 0:
        if guitar > g_cnt:
            guitar = g_cnt

    for j in range(x+1, N):
        DFS(j, temp[:], s_cnt, g_cnt + 1)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    song = []
    A, B = input().split()
    for b in B:
        if b == 'Y':
            song.append(1)
        else:
            song.append(0)
    arr.append((A, song))

max_cnt = 0 # 최소값으로 초기화
guitar = 11 # 최대값으로 초기화

for i in range(N):
    temp = [0] * M
    DFS(i, temp)

if guitar == 11:
    print(-1)

else:
    print(guitar)
