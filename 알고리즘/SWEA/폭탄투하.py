import pprint
arr = [['_' for _ in range(5)] for _ in range(4)]

for _ in range(2):
    y, x = map(int, input().split())
    position = [-1, 0, 1]
