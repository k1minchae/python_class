import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
text = input().rstrip()

# 패턴 생성
pattern = 'I' + 'OI' * N

cnt = 0

LPS = [0] * (2 * N + 1) # 패턴의 길이만큼 lps리스트 만들기
i = 1
n_idx = 0   # 검사할 인덱스 번호
while i < 2 * N + 1:
    if pattern[i] == pattern[n_idx]:    # 같은 경우 다음 인덱스 검사
        n_idx += 1
        LPS[i] = n_idx  # lps에 인덱스 저장
        i += 1
    else:   # 같지 않은 경우
        if n_idx:   # 이전에 같았던 인덱스로 돌아가서 검사
            n_idx = LPS[n_idx-1]
        else:
            i += 1

t_idx = 0
p_idx = 0
while t_idx < M:
    if pattern[p_idx] == text[t_idx]:
        t_idx += 1
        p_idx += 1
        if p_idx == 2 * N + 1:
            cnt += 1
            p_idx = LPS[p_idx-1]
    else:
        if p_idx:
            p_idx = LPS[p_idx-1]
        else:
            t_idx += 1

print(cnt)
