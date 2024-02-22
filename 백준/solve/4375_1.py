# 1
import sys
input = sys.stdin.readline
while True:
    try:
        n = int(input())
        result = '1'
        while int(result) % n != 0:
            result += '1'
        print(len(result))
    except:
        break