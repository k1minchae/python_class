N = int(input())
count = 0
def fac(x):
    if x <= 1:
        return 1
    else:
        return x * fac(x-1)

num = [*str(fac(N))]
num.reverse()

for i in num:
    if i == '0':
        count += 1
    else:
        break
print(count)
