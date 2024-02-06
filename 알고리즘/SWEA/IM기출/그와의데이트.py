D = list(map(str, input().split('.')))

cnt_m = 1
cnt_d = 1


# 월
if 'X' == D[1]: # 월이 한자리수
    cnt_m = 9
elif 'X' == D[1][1]: # 두자리수
    cnt_m = 3

# 일
if 'X' == D[2]: # 일이 한자리수
    cnt_d = 9
elif 'XX' == D[2]: # 일이 두자리수
    cnt_d = 22
elif '3X' == D[2]: # 30, 31
    cnt_d = 2
elif 'X' == D[2][1]: # 두자리수인데 일의자리 X
    cnt_d = 10
elif 'X0' == D[2] or 'X1' == D[2]:
    cnt_d = 3
elif 'X' == D[2][0]: # 30, 31 아닌경우
    cnt_d = 2
result = cnt_m * cnt_d
print(result)
