# import sys
#
# a = ''
# b = 'h'
#
# print(sys.getsizeof(a)) # string 빈칸의 사이즈 : 49 (항상 49는아님)
# print(sys.getsizeof(b)) # 1바이트 추가 -> 50

# 문자열 비교

T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

