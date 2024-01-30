N = int(input())
list = []
for _ in range(N):
    x = int(input())
    list.append(x)
    
for i in range(N-1, 0, -1):
    for j in range(i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
for k in list:
    print(k)