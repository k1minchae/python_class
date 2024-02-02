A, B = map(int, input().split())
cnt = 0
while A < B:
    if B % 2 == 0:
        B = B // 2
        cnt += 1
    else:
        if str(B)[-1] == '1':
            B = str(B)[:-1]
            B = int(B)
            cnt += 1
print(cnt)
