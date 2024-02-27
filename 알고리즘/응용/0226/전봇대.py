# 전봇대
# 내 코드 (오답)
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 전선의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for line1 in arr:
        for line2 in arr:
            if min(line1[0], line1[1]) < line2[0] < max(line1[0], line2[1]) or min(line1[0], line1[1]) < line2[1] < max(line1[0], line1[1]):
                cnt += 1
    print(f'#{tc} {cnt}')

'''
A - B 를 잇는 경우, 
1 ~ (A-1) 사이에 B보다 큰 것을 counting

target -> A전봇대에서 가장 큰 정수 

예시 : 4-3 을 잇는 경우
target = 4
1~3 사이에 3보다 큰 것을 counting
'''
# 강사님 코드
def get_result():
    # 리스트 arr : 튜플 형태로 a전봇대와 b전봇대를 저장할 리스트
    size = len(arr)
    cnt = 0
    for i in range(size):
        for target in range(i):
            # a 전봇대 : 튜플의 첫번째 요소, b 전봇대 : 튜플의 두번째 요소
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[target][0], arr[target][1])
            if i_b < tar_b:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input())    # a전봇대, b전봇대
        arr.append((a, b))

    # 함수 호출 전에 정렬
    arr.sort(key=lambda x: x[0])
    result = get_result()
    print(f'#{tc} {result}')

# 다른 풀이법
T = int(input())
for t in range(1, T+1):
    N = int(input())
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (temp[i][0]-temp[j][0])*(temp[i][1]-temp[j][1])<0:
                cnt += 1
    print(f'#{t} {cnt}')