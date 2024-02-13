# 평행사변형
import sys

Xa, Ya, Xb, Yb, Xc, Yc = map(int, sys.stdin.readline().split())

if Xa == Xb or Xa == Xc or Xb == Xc or Ya == Yb or Ya == Yc or Yb == Yc:

    AB = ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** 0.5
    AC = ((Xa - Xc) ** 2 + (Yc - Ya) ** 2) ** 0.5
    BC = ((Xb - Xc) ** 2 + (Yc - Yb) ** 2) ** 0.5

    arr = sorted([AB, AC, BC])
    D = []
    D.append(arr[-1] * 2 + arr[0] * 2)
    D.append(arr[-1] * 2 + arr[1] * 2)
    D.append(arr[0] * 2 + arr[1] * 2)

    print(max(D) - min(D))

else:
    print(-1)