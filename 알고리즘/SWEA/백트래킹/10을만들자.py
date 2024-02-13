# 10을 만들자
from itertools import product
                    # 순열 : 원소중복 O
N = int(input())
numbers = [i for i in range(1, 10)]
N_list = list(product(numbers, repeat=N))

cnt = 0
for n in N_list:
    if sum(n) == 10:
        cnt += 1

print(cnt)