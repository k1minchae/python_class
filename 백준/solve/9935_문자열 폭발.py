# 문자열 폭발
import sys
input = sys.stdin.readline
S = input().rstrip()
X = list(input().rstrip()) # 폭발 문자열
L = len(X) # 폭발 문자열의 길이
result = []
stack = []

for s in S:
    result.append(s) # 일단 결과에 저장하고 시작
    if s not in X: # 만약 폭발문자열에 속하지 않는다면
        stack.clear() # 폭발할 수 없으므로 stack 초기화
        continue
    else: # 폭발문자열에 속한다면
        stack.append(s) # stack에 추가

        # 폭발할 수 있는지 판별
        # 길이가 폭발문자열만큼은 되어야하고, 맨끝이 폭발문자열이어야함
        if len(stack) >= L and stack[-L:] == X: # 폭발 가능하다면
            for i in range(L):
                stack.pop() # 스택에서도 날려주고
                result.pop() # 결과 배열에서도 폭발시켜줌

if not result: # 결과 배열이 비어있다면 FRULA출력
    print('FRULA')
else: # 아니라면 문자열 붙여서 출력
    for r in result:
        print(r, end='')
