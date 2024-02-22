# 괄호 검사
T = int(input())
for tc in range(1, T+1):
    S = input()

    def stack_test(S):
        stack = []
        for s in S:
            if s == '{' or s == '(':
                stack.append(s)
            if s == '}':
                if stack == [] or stack.pop() != '{':
                    return 0
            if s == ')':
                if stack == [] or stack.pop() != '(':
                    return 0

        if stack == []:
            return 1
        else:
            return 0

    result = stack_test(S)
    print(f'#{tc} {result}')


