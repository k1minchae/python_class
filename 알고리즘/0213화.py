# 계산기
# fx = '(6+5*(2-8)/2)'
# top = -1
# stack = [0] * 100
#
# icp = {'(': 3, '*': 2, '/':2, '+':1, '-':1} # 스택에 들어오기 전
# isp = {'(': 0, '*': 2, '/':2, '+':1, '-':1} # 스택에 들어온 후
# postfix = '' # 우리가 구하려는 후위식
# for tk in fx:
#     # 여는 괄호 push, top 원소보다 우선순위가 높으면 push
#     if tk == '(' or isp[stack[top]] < icp[tk]:
#         top += 1 # push
#         stack[top] = tk # append 로 해도 됨
#
#     # 연산자이고 top원소보다 우선순위가 높지 않으면
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
#         # top원소의 우선순위가 더 낮을 때까지 pop
#         while isp[stack[top]] >= icp[tk]:
#             top -= 1 # pop
#             postfix += stack[top+1]
#         top += 1 # push
#         stack[top] = tk
#     elif tk == ')':
#         while stack[top] != '(':
#             top -= 1 # pop
#             postfix += stack[top+1]
#         top -= 1 # 여는 괄호 pop해서 버림
#         stack[top+1]
#     else: # 피연산자인경우
#         postfix += tk
# print(postfix)

# 부분집합
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end= ' ')
#         print()
#     else:
#         # for j in range(2):
#         #     bit[i] = j
#         #     f(i+1, k)
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
# N = 4
# arr = [1, 2, 3, 4]
# bit = [0] * 4 # bit[i] : arr[i] 가 부분집합에 포함되었는지를 나타내는 배열
# f(0, N) # bit[i] 에 1 또는 0을 채우고 N 개의 원소가 결정되면 부분집합을 출력
# '''출력
#  # 공집합
# 4
# 3
# 3 4
# 2
# 2 4
# 2 3
# 2 3 4
# 1
# 1 4
# 1 3
# 1 3 4
# 1 2
# 1 2 4
# 1 2 3
# 1 2 3 4
# '''

# 후위표기법
#
# S = input()
# stack = []
#
# for s in S:
#     if '0' <= s <= '9':
#         stack.append(int(s))
#     else:
#         a = stack.pop()
#         b = stack.pop()
#         if s == '+':
#             stack.append(b+a)
#         else:
#             stack.append(b-a)
# print(stack[-1])


