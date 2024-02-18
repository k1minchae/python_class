# 잃어버린 괄호
import sys
input = sys.stdin.readline
X = input().rstrip()
stack = []
for x in X:
    if x not in '+-':
        stack.append(x)
