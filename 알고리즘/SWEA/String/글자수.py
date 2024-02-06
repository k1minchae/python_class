T = int(input())
for tc in range(1, T+1):
    str1 = set(map(str, input()))
    str2 = input()

    max_cnt = float('-inf')

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')

# 강사님 코드
# result = int(str1 in str2)
# print(f'#{tc} {result}')