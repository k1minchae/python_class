n, m = list(map(int, input().split()))

# 할당활용하기
x = 1

for i in range(1, (min(n, m))+1):
    if ((n % i) == 0) and ((m % i) == 0): 
        x = i
    else:
        continue
max_number = x # 최대공약수
min_number = n * m / x # 최소공배수

print(max_number)
print(min_number)
