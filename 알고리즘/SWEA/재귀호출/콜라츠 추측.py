N = int(input())
cnt = 0
def col(N):
    global cnt
    if N == 1:
        return cnt
    else:
        if N % 2 == 0:
            N /= 2
            cnt += 1
            return col(N)
        else:
            N = N * 3 + 1
            cnt += 1
            return col(N)
result = col(N)
print(result)