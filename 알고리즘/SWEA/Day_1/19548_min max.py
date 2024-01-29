def max_min(a_list):
    return max(a_list) - min(a_list)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a_list = list(map(int, input().split()))
    
    result = max_min(a_list)
    print(f'#{tc} {result}')