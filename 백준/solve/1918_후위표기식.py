# 후위 표기식
import sys
input = sys.stdin.readline
S = input().rstrip()

def postfix(S):
    stack = []
    result = []
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for s in S:
        if s.isalnum():  # 연산자 아님
            result.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '(' 제거

        else:  # 연산자
            while stack and priority.get(stack[-1], 0) >= priority[s]: # 우선순위 낮거나 같을때동안은 pop
                result.append(stack.pop())
            stack.append(s) # 우선순위 높아질 때 push

    while stack:
        result.append(stack.pop())

    return ''.join(result)

print(postfix(S))