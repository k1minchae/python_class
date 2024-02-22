# 회문
def is_p(string):
    return string[::-1]

def find_p(N, M, arr):
    for i in range(N):
        # 각 행에서 가능 시작 위치, M길이의 회문을 찾기 위해서 N-M위치까지만 고려
        for j in range(N-M+1):
            # 가로 회문 --> 시작 j에서 길이가 M 만큼의 부분 문자열
            h = arr[i][j : j+M]
            if h == is_p(h):
                print(f'#{tc} {"".join(h)}')

            # 세로 회문 k행 i 열의 문자열 가져오기
            v = [arr[k][i] for k in range(j, j+M)]
            if v == is_p(v):
                print(f'#{tc} {"".join(v)}')
            # 회문 판별
            # is_p

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    find_p(N, M, arr)