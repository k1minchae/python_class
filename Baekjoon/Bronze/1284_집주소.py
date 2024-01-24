# 여백 = 숫자 갯수 + 1
# 0 = 4cm, 1 = 2cm, 나머지 = 3cm

import sys

while True:
    N = int(sys.stdin.readline().strip())
    num_list = []
    num_list.extend(str(N))
    wid = len(str(N)) + 1

    if N == 0:
        break
    else:
        wide = []
        for i in num_list:
            if i == '0':
                wide.append(4)
            elif i == '1':
                wide.append(2)
            else:
                wide.append(3)
        print(sum(wide) + wid)


