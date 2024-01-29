import sys

N = int(sys.stdin.readline())
number = []


while True:
    # 모든 요소에 대해 적용할 때 쓰는것 : all
    if all((j == '4') or (j == '7') for j in str(N)):
        print(N)
        False
        break
    else:
        N= N-1