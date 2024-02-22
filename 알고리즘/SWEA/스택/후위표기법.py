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
    #     a = int(스택.pop())
    #     b = int(스택.pop())
    #     스택.append(a+b)
    # elif s == '-':
    #     a = int(스택.pop())
    #     b = int(스택.pop())
    #     스택.append(b-a)
    # elif s == '*':
    #     a = int(스택.pop())
    #     b = int(스택.pop())
    #     스택.append(b * a)
    # else:
    #     a = int(스택.pop())
    #     b = int(스택.pop())
    #     스택.append(b / a)
print(*stack)