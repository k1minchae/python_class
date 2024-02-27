T = int(input())
def reverse_(x):  # 돌을 뒤집는 함수
    if x == 1:
        return 0
    if x == 0:
        return 1

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        I, J, W = map(int, input().split()) # 기준위치, 작업할 돌의 개수, 수행할 작업

        if W == 1: # 1번 작업
            for i in range(I-1, I-1+J):
                if 0 <= i < N:  # 범위 안에 있는 돌을
                    arr[i] = reverse_(arr[i]) # 전부 뒤집는다

        elif W == 2: # 2번 작업
            for i in range(I-1, I-1+J):
                if 0 <= i < N:  # 범위 안의 돌을
                    arr[i] = arr[I-1]  # 전부 i번째 돌의 색으로 바꾼다

        elif W == 3: # 3번 작업
            for i in range(1, J+1):
                if 0 <= I-1+i < N and 0 <= I-1-i < N:
                    if arr[I-1+i] == arr[I-1-i]: # 마주보는 돌의 색이 같으면
                        arr[I-1+i] = arr[I-1-i] = reverse_(arr[I-1+i]) # 뒤집는다
    print(f'#{tc}', *arr)
