S = input()

stack = []
result = ''

for s in S:
    if s not in '+-/*':
        stack.append(s)
    else:
        a = int(stack.pop())
        b = int(stack.pop())

    # elif s == '+':
    #     a = int(stack.pop())
    #     b = int(stack.pop())
    #     stack.append(a+b)
    # elif s == '-':
    #     a = int(stack.pop())
    #     b = int(stack.pop())
    #     stack.append(b-a)
    # elif s == '*':
    #     a = int(stack.pop())
    #     b = int(stack.pop())
    #     stack.append(b * a)
    # else:
    #     a = int(stack.pop())
    #     b = int(stack.pop())
    #     stack.append(b / a)
print(*stack)