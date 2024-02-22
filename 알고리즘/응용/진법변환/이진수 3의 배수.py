# 이진수 3의 배수
N, K = map(int, input().split())
def comb(n, k): # 조합
    case=1
    for j in range(k):
        case *= n-j
        case //= j + 1
    return case

result = 0
for i in range(K+1):
    one = i
    two = K - i
    if one <= (N+1)//2 and two <= N//2: # 유효한 최대 개수 안이라면
        if (one + 2 * two) % 3 == 0: # 3의 배수
            result += comb((N+1)//2, one) * comb(N//2, two)
            # (1을 넣을 수 있는 자리수, 1의 개수)
            # (2를 넣을 수 있는 자리수, 2의 개수)
            # 각 조합을 곱해서 최종 경우의수에 더함

print(result)