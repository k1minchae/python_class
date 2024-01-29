# import datetime

# H, M = map(int, input().split())

# # 입력으로 받은 시간과 분을 사용하여 datetime 객체 생성
# input_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, H, M)

# # 45분을 빼기 위해 timedelta 객체 생성
# time_difference = datetime.timedelta(minutes=45)

# # 입력 시간에서 45분 전의 시간을 계산
# result_time = input_time - time_difference

# # 결과 출력
# print(result_time.time().strftime('%H %M').lstrip('0'))
# # strftime -> '%H시 %M분 %S초'
# #lstrip('0') : 문자열앞의 0 제거

H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 23
        M = M + 15
    else:    
        H = H - 1
        M = M + 15
else:
    M = M - 45

print(f'{H} {M}')