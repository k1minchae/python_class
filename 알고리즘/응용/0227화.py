# # 1111 ~ 3333 까지 출력하는 코드 작성
# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for g in range(1, 4):
#                 print(i, j, k, g)
# '''
# 1 1 1 1
# 1 1 1 2
# 1 1 1 3
# 1 1 2 1
# 1 1 2 2
# 1 1 2 3
#
# 생략 ...
#
# 3 3 2 1
# 3 3 2 2
# 3 3 2 3
# 3 3 3 1
# 3 3 3 2
# 3 3 3 3
# '''
# def BBQ(x):
#     x += 10
#     print(x)
#
# def KFC(x):
#     print(x)
#     x += 3
#     BBQ(x+2)
#     print(x)
#
# x = 3
# KFC(x+1)
# print(x)
#
# '''
# 결과: 4 -> 19 -> 7 -> 3
# '''

# def recursion(x):
#     if x == 6:
#         return
#     print(x, end = ' ')
#     recursion(x+1)
#     print(x, end = ' ')
#
# recursion(0)
# # 0 1 2 3 4 5 5 4 3 2 1 0

# def KFC(x):
#     if x == 3:
#         return
#     for i in range(4):
#         KFC(x + 1)
# KFC(0)

# path = []
#
# def recursion(x):
#     if x == 2:
#         print(*path)
#         return
#     for i in range(3):
#         path.append(i)
#         recursion(x + 1)
#         path.pop()  # 기록 삭제
# recursion(0)
# '''
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# '''


# temp = []
# visited = [0] * 3   # branch 의 개수만큼
# def permutation(x):
#     if x == 2:
#         print(*temp)
#         return
#     for i in range(3):
#         if visited[i]:
#             continue
#         visited[i] = 1  # 기록
#         temp.append(i)
#         permutation(x+1)
#         temp.pop()
#         visited[i] = 0  # 삭제
# permutation(0)
#
# '''
# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1
# '''
# temp = []
# def per(x): # 중복 O (Type 1)
#     if x == 2:
#         print(*temp)
#         return
#     for i in range(1, 7):
#         temp.append(i)
#         per(x+1)
#         temp.pop()
#
# per(0)