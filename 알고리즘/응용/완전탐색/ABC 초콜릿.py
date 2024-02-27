# ABC 초콜릿
# 내 코드
N = int(input())
result = 0

def ABC(s, x, cnt): # 시작값, 레벨, 연속된 수 cnt
    global result
    if cnt >= 3:
        return
    if x == N:
        result += 1
        return
    for n in range(3):
        if s == n:  # 시작값이 다음값과 같으면
            ABC(n, x+1, cnt+1) # cnt + 1
        else:
            ABC(n, x+1, 1)  # 아니면, cnt = 1

ABC(-1, 0, 0) # -1 부터 시작해서 시작값을 정하지 않고 시작
print(result)

# 강사님 코드
result = 0
path = [''] * 3
n = int(input())
def cnt(level):
    if level < 3:
        return True
    if path[level-3] != path[level-2]:
        return True
    if path[level-2] != path[level -1]:
        return True
    return False

def run(level):
    global result
    if not cnt(level):
        return  # 가지치기
    if level == n:
        result += 1
        return

    for i in range(3):
        path[level] = chr(ord('A') + i) # 아스키 코드로 바꾸고 정수 더하고 문자로 바꿈
        # A B C 가 연속된 숫자라서
        run(level + 1)
        path[level] = ''

run(0)
print(result)