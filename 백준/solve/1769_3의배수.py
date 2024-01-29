# 재귀함수 연습
def three(x, count):
    if int(x) <= 9:
        if int(x) % 3 == 0:
            return print(count), print('YES')
        else:
            return print(count), print('NO')
    count += 1
    return three(str(sum(map(int, [*x]))), count)

three(input(), 0)
