T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split()) # 책은 1쪽~P쪽, A가 찾을 쪽, B가 찾을쪽

    start_A = 1
    end_A = P
    start_B = 1
    end_B = P

    def binary_count(start_page, end_page, find_page):
        count_var = 0
        while start_page <= end_page:
            count_var += 1
            c = (start_page + end_page) // 2 # 중앙값
            if c == find_page: # 탐색 성공
                return count_var
            elif find_page > c: # 찾을 페이지가 중앙기준 오른쪽에 있으면
                start_page = c
            else:   # 왼쪽에있으면
                end_page = c
        return count_var
    A_result = binary_count(start_A, end_A, A)
    B_result = binary_count(start_B, end_B, B)

    if A_result < B_result:
        result = 'A'
    elif B_result < A_result:
        result = 'B'
    else:
        result = '0'

    print(f'#{tc} {result}')
