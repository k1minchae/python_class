# 스택
import sys
N = int(input())
stack = []
def f(S):
    if 'push' in S:
        stack.append(S.split()[1])
    elif 'pop' in S:
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in S:
        print(len(stack))
    elif 'empty' in S:
        if stack != []:
            print(0)
        else:
            print(1)
    elif 'top' in S:
        if stack != []:
            print(stack[-1])
        else:
            print(-1)
for _ in range(N):
    f(sys.stdin.readline().strip('\n'))
