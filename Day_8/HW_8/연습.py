# max 함수 안쓰기
a = [4, 5, 6, 1, 2]
x = a[0]
for i in a:
    if i > x:
        x = i
print(x)

# min 함수 안쓰기
b = [2, 4, 1, 9, 3]
y = b[0]
for j in b:
    if j < y:
        y = j
print(y)

# sum 함수 안쓰기
c = [1, 3, 4, 5, 2] # 15
for k in c:
    