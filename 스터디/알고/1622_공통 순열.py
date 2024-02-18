# 1622 : 공통 순열
while True:
    try:
        a = sorted(list(input()))
        b = list(input())
        result = ''
        for A in a:
            if A in b:
                b.remove(A)
                result += A
        print(result)
    except:
        break