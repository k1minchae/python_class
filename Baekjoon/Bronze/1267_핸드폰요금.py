import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

y_list = []
m_list = []

for i in time:
    y_list.append((i // 30 + 1) * 10) 
    m_list.append((i // 60 + 1) * 15)

if sum(y_list) < sum(m_list):
    print(f'Y {sum(y_list)}')
elif sum(y_list) > sum(m_list):
    print(f'M {sum(m_list)}')
else:
    print(f'Y M {sum(y_list)}')
