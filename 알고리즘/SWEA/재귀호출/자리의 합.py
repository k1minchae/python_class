N = int(input())
def my_sum(N):
    if N < 10:
        return N
    else:
        n = N % 10
        not_n = N // 10
        return n + my_sum(not_n)
result = my_sum(N)
print(result)