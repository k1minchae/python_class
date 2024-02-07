'''라이브 강의 : 재귀 호출
def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

def fibo_memo(n):
    global cnt
    cnt += 1
    if n != 0 and memo[n] ==0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]

cnt = 0
n = 7
print(fibo(7), cnt) # 13 41 -> 41 번 호출
memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n), cnt) # -> 13 번 호출


# 여기서부터 강사님 문제풀이
# 자동 수학 계산기
ex = input()

# 첫 번째 문자가 음수가 안되도록 처리
if ex[0] == '-':
    ex = '0' + ex

word = ex.split('+') # 덧셈 기호를 기준으로 분리
result = 0
for w in word:
    # 뺄셈 기호를 기준으로 분리
    w = w.split('-')

    # 첫 번째 요소는 더해줄 값
    inner_ans = int(w[0])

    # 나머지 요소들은 빼줄 값
    for i in range(1, len(w)):
        inner_ans -= int(w[i])

    result += inner_ans
print(result)

# 내장함수로 쓰는 법
print(eval(input()))


# 종이 붙이기
# n = 10일 때 1, n = 20일 때 3, n = 30일 때 5, 11, ...
# a(n) = a(n-20) * 2 + a(n-10)
def cnt(n):
    if n % 10 == 0:
        if n == 10: # 종료조건 1
            return 1
        elif n == 20: # 종료조건2
            return 3
        else: # n >20 일 때 n-20에서의 경우의수 2배와 n-10에서의 경우의수의 합
            return cnt(n-10) + 2 * cnt(n-20)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = cnt(n)
    print(result)

'''

# 멋진 AB
n = int(input())

cnt = 0
for _ in range(n):
    word = input()
    stack = []

    for char in word:
        if not stack: # 스택이 비어있으면 문자 추가
            stack.append(char)
        elif char == stack[-1]: # 스택의 마지막 요소가 현재 문자와 같으면 pop
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        cnt += 1 # 스택이 비어있으면 카운트 증가
print(cnt)