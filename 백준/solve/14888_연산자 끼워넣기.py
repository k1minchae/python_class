# 연산자 끼워넣기 : 14888
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))  # + - * /

min_v = float('inf')
max_v = float('-inf')

def BTC(s, num = arr[0]):
    global min_v, max_v
    if s == N-1:
        if num < min_v:
            min_v = num
        if num > max_v:
            max_v = num
        return
    for k in range(4):
        if op[k] > 0:
            op[k] -= 1
            if k % 4 == 0:
                BTC(s+1, num+arr[s+1])
            elif k % 4 == 1:
                BTC(s+1, num - arr[s+1])
            elif k % 4 == 2:
                BTC(s+1, num * arr[s+1])
            else:
                if num < 0:
                    BTC(s+1, -(-num // arr[s+1]))
                else:
                    BTC(s+1, num // arr[s+1])
            op[k] += 1
BTC(0)
print(max_v)
print(min_v)