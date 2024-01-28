import sys

count_P = {} # 광합성O
count_M = {} # 운동성X
a_list = []
whole_a_list = []

N, M = map(int, sys.stdin.readline().split())

for i in range(M):
    a, b, c = map(str, sys.stdin.readline().strip('\n').split())
    a_list.append(int(a))
    if (b == 'P') and (c == '1'): # 광합성O 딕셔너리에 넣기.
        count_P[a] = count_P.get(a, 0) + 1
    elif (b == 'M') and (c == '0'):
        count_M[a] = count_M.get(a, 0) + 1

a_list_ = list(set(a_list)) # 중복된 a 가 카운트되지 않도록 set -> list과정 거침




c_min = abs((sum(count_P.values())) - (sum(count_M.values())))


for j in count_M:   # 중복값제거
    count_P.pop(j, None)
print(sum(whole_a_list))
print(sum(a_list_))
c_max = sum(count_M.values()) + sum(count_P.values()) + N - len(a_list_)

print(f'{c_min} {c_max}')


# 확실한것:
# 확실히아닌것 으로나눠서 다시해보기

'''
	
정답코드

import sys
n, m = map(int, sys.stdin.readline().split())

live_dict = {} # key: 이름-기능 / value: 기능유무
certainly_ = []
never = []

for i in range(m):  # 실험수 : m만큼 순회
    str_tmp = ''.join(sys.stdin.readline().split())
    # 입력값: 생물number 기능종류(P-광)(M-운동) 기능유무

    live_dict[str_tmp[:-1]] = str_tmp[-1]
    
for k, v in live_dict.items():
    a, b, c = k[:-1], k[-1], v

    if b == 'P':    # 광합성
        if c == '1':
            certainly_.append(a)
        else:
            never.append(a)
    else:   # 운동성
        if c == '0':
            certainly_.append(a)
        else:
            never.append(a)

certain = 0

for live_thing in set(certainly_):  # 확실한것 : 광합성O 운동성X
    if certainly_.count(live_thing) == 2:
        certain += 1

max_ = n - len(set(never))

print(certain, max_)
'''