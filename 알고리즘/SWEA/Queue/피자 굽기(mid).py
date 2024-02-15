from collections import deque

def cooking():
    if len(dq) == 1:    # 화덕에 하나 남았을 때 종료
        return dq[0][0]
    cooked = dq.popleft()   # 맨앞에 피자 빼기
    cooked = (cooked[0], cooked[1] // 2) # 치즈 녹은 값 반영
    if cooked[1] == 0:  # 치즈가 다 녹았으면
        if un_cooked_dq:    # 요리 안한 피자가 있으면
            new_pz = un_cooked_dq.popleft() # 요리안한 덱에서 뽑아서
            dq.append(new_pz)   # 화덕에 추가
        return cooking()
    else:   # 치즈가 안녹았으면
        dq.append(cooked)   # 피자 화덕에 넣기
        return cooking()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 화덕 : N // 피자 개수 : M
    arr = [(idx, cheese) for idx, cheese in enumerate(list(map(int, input().split())))]

    dq = deque(arr[:N]) # 처음 요리할 피자들
    un_cooked_dq = deque(arr[N:])

    result = cooking() + 1
    print(f'#{tc} {result}')