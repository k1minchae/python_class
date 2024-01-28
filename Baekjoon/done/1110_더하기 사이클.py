N = int(input())
number = N  # 처음 입력값을 number에 저장한 뒤 계산
count = 0   # while 문을 돌린 횟수

while True:
    a = number // 10    # 10의자리수
    b = number % 10     # 1의 자리수
    c = (a+b) % 10  # 첫번째 계산을 한 뒤 1의 자리수
    number = b * 10 + c

    count += 1

    if number == N:
        break

print(count)