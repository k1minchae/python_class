# '''
# 수를 입력받고 암호화 복호화 해주는 프로그램 제작
# KEY값은 1004
# 1.수 1000을 인코딩 하여 출력
# 2. 4를 디코딩하여 출력
# '''
# KEY = 1004
#
# def en_decode(num):
#     return num ^ KEY
# print(en_decode(1000))  # 4
# print(en_decode(4))     # 1000

'''
Left shift << 를 이용한 프로그래밍
반복문을 이용하여 출력
0b 1 출력 ( 2진수와 10진수로 )
0b 10 출력
0b 100
0b 1000
0b 10000
'''
# for i in range(5):
#     x = 0b1 << i
#     print(bin(x), x)
'''
0b1 1
0b10 2
0b100 4
0b1000 8
0b10000 16
'''
# SWEA 10726 이진수표현
# def f():
#     tar = M
#     for i in range(N):
#         if tar & 0b1 == 0:
#             return 'OFF'
#         tar = tar >> 1
#     return 'ON'
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     print(f'#{tc} {f()}')
print(f'{0.1:.20f}') # 0.10000000000000000555