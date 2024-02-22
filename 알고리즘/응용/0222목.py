# 리스트에 숫자 넣기
# '''
# 수 N 을 입력받는다.
# 윗줄에는 N부터 1씩 증가하는 숫자 4개를 왼쪽에 채운다.
# 아랫줄에는 N부터 1씩 감소되는 숫자 4개를 오른쪽에 채운다.
# 이 숫자를 2x7 행렬에 채운다.
# 최종결과를 출력한다. 빈 공간은 0으로 출력한다.
# '''
# N = int(input())
# arr = [[0] * 7 for _ in range(2)]
#
# t1 = N
# for i in range(4):
#     arr[0][i] = t1
#     t1 += 1
#
# t2 = N
# for i in range(6, 2, -1):
#     arr[1][i] = t2
#     t2 -= 1
# print(arr[0])
# print(arr[1])

# n = int(input())
#
# for i in range(50):
#     print(i)
# 50번 반복 => 상수 배수는 하지 않기 때문에 O(1)

# import sys
# sys.stdin = open('input.txt', 'r') # r: 파일을 읽는다는 뜻
# N = int(input())
# print(N)
# '''
# 두 수를 input.txt 파일에서 입력받는다.
# 두 수의 합과 곱을 output.txt 파일에 출력한다.
# '''
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#
# a, b = map(int, input().split())
# print(a * b)

# tar = 75
# result = []
#
# while tar:
#     result.append(tar%2)
#     tar //= 2
#
# result.reverse()
# print(*result) # 1 0 0 1 0 1 1



''' 이진수
1. 진수표 활용
2. 16진수 -> 10진수 -> 2진수
3. 파이썬 내장 함수 사용
'''

# 3번
T = int(input())
for tc in range(1, T+1):
       N, hex = input().split()
       dec = int('0x'+hex, 16) # 16진수를 10진수로 바꾸기
       bin = format(dec, 'b') # 10진수를 2진수로 바꾸기

       if len(bin) < int(N) * 4:
              bin = '0' + bin
              print(f'#{tc} {bin}')

# 2진수2

T = int(input())

for tc in range(1, T+1):
       n = float(input())
       cnt = 0
       bin = ''
       while n > 0:
              temp = n * 2
              bin += str(temp)[0] # temp의 정수부분을 이진수(bin)에 추가
              n = temp - int(temp) # 정수부분을 빼고 남은 소수부분을 다시 n에 할당
              cnt += 1 # 자릿수

              if cnt > 12:  # 이진수 자릿수가 12자리 넘어가면
                     break
       if cnt > 12:
              print(f'#{tc} overflow')
       else:
              print(f'#{tc} {bin}')