# 재귀함수 연습
def binery(N):
    if N > 1:
        binery(N // 2)
    return print(N % 2, end = '')
binery(int(input()))