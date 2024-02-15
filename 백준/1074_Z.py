# Z
import sys
num = 0
def Z(n, x, y):
    global num

    half_line = 2 ** (n-1)

    if n == 1:
        num += 2 * y + x
        return

    if y >= half_line:
        y -= half_line

        if x >= half_line:
            num += 3 * (half_line **2)
            x -= half_line
        else:
            num += 2 * (half_line ** 2)

    elif x >= half_line:
            num += (half_line ** 2)
            x -= half_line

    return Z(n-1, x, y)

N, r, c = map(int, sys.stdin.readline().split())
Z(N, c, r)
print(num)