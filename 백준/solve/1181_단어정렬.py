# 시간초과 코드
# import sys

# N = int(sys.stdin.readline())
# word_list = []
# for _ in range(N):
#     word = sys.stdin.readline().strip('\n')
#     word_list.append(word)

# word_list = list(set(word_list))
# word_list.sort()

# # 버블 정렬
# for i in range(len(word_list)-1,0,-1):
#     for j in range(i):
#         if len(word_list[j]) > len(word_list[j+1]):
#             word_list[j], word_list[j+1] = word_list[j+1], word_list[j]

# for k in word_list:
#     print(k)
    
    
# 다시 풀기
import sys
N = int(sys.stdin.readline())
word_list = []
for _ in range(N):
    x = sys.stdin.readline().strip('\n')
    word_list.append(x)
word_list = list(set(word_list))

# 길이순 -> 오름차순 
word_list.sort(key=lambda x: (len(x), x.lower()))

for i in word_list:
    print(i)