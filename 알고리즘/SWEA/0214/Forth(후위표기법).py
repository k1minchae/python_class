# Forth(후위표기법)

T = int(input())
for tc in range(1, T+1):
    S = list(input().split())
    stack = []
    not_num = '+-/*'
    result = ''
    for s in S:
        if s == '.':
            break
        if s not in not_num and s != '.':    # 숫자라면
            stack.append(s)
        else:   # 연산자라면
            if len(stack) < 2:  # 숫자를 못 꺼내오는 경우
                result = 'error'
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if s == '+':
                    stack.append(b + a)
                elif s == '-':
                    stack.append(b - a)
                elif s == '/':
                    if a == 0:
                        result = 'error'
                        break
                    stack.append(b//a)
                elif s == '*':
                    stack.append(b * a)
                else:
                    break

    if result != 'error' and len(stack) == 1:
        print(f'#{tc} {stack[0]}')
    elif len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {result}')