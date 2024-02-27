# 다섯종류의 숫자카드
C = input()
path = [0] * 5
cnt = 0
def cards(x):   # 레벨: x
    global cnt
    if x > 1 and abs(int(path[x-1]) - int(path[x-2])) > 3:
        return
    if x == 4:
        cnt += 1
        return
    for i in range(5):  # branch : 5
        path[x] = C[i]
        cards(x+1)
        path[x] = 0

cards(0)
print(cnt)