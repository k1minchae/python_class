N = int(input())

# 팩토리얼 재귀함수
def fac(x):
    if x == 0:
        return 1
    elif x == 1:
        return x
    return x * fac(x-1)    

result =fac(N)
print(result)