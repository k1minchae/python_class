# 반복문자 지우기
T = int(input())
for tc in range(1, T+1):
    S = input()
    stack = []
    for s in S:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    print(f'#{tc} {len(stack)}')