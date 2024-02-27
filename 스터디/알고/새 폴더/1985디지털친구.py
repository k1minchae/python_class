# 1985 : 디지털 친구
import sys
input = sys.stdin.readline

def friends(x, y):
    for i in range(len(y)-1):
        y[i] = y[i] + 1
        y[i+1] = y[i+1] - 1
        if set(y) == set(x):
            return True
        y[i] = y[i] - 2
        y[i+1] = y[i+1] + 2
        if i != 0 or y[i] != 0:
            if set(y) == set(x):
                return True
        y[i] = y[i] + 1
        y[i+1] = y[i+1] - 1
    if set(x) ==set(y):
        return True
    else:
        return False

for _ in range(3):
    x, y = input().split()
    X = list(map(int, x))
    Y = list(map(int, y))

    if set(X) == set(Y):
        print('friends')
    else:
        if friends(X,Y) or friends(Y,X):
            print('almost friends')
        else:
            print('nothing')