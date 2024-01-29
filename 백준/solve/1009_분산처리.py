import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    aa = a % 10

    if aa == 0: # 0
        print(10)
    elif aa == 1 or aa == 5 or a == 6:
        print(aa)
    elif aa == 2 or aa == 3 or aa == 7 or aa == 8:
        if b % 4 == 1:
            print(aa)
        elif b % 4 ==2:
            print((aa * aa) % 10)
        elif b % 4 ==3:
            print((aa ** 3) % 10)
        else:
            print((aa ** 4) % 10)
    else:
        if b % 2 == 1:
            print(aa)
        else:
            print((aa ** 2) % 10)
