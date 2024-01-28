T = int(input())

import sys

for _ in range(T):
    message = list(map(list, sys.stdin.readline().strip('\n').split()))
    word = [] # 각 단어를 뒤집어서 저장한 2차원 리스트
    for i in message:
        word.extend(list(reversed(i)))
        word.append(' ')
    
    print(''.join(word))
