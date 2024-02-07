# 괄호
T = int(input())
for _ in range(T):
    S = input()

    def check(S):
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            if s == ')' and stack == []:
                return 'NO'
            if s == ')' and stack != []:
                stack.pop()
        if stack:
            return 'NO'
        else:
            return 'YES'

    result = check(S)
    print(result)