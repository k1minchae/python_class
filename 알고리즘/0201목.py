# 이진탐색
'''
def bs(pages, p):
    s = 1 # 탐색 시작점
    e = pages # 탐색 끝점
    mid = 0
    cnt = 1  # 첫번째 탐색 포함
    # 찾고자하는 값(p)를 찾을 때까지 반복
    while p != mid:
        mid = (s + e) // 2  # 1.중간값 계산
        if mid > p: # 왼쪽 탐색
            e = mid
        else: # 오른쪽 탐색
            s = mid
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A = bs(P, Pa)
    B = bs(P, Pb)
    if A == B:
        result = 0
    elif A < B:
        result = 'A'
    else:
        result = 'B'
    print('#{tc} {result}')
    # start = middle + 1 --> 이렇게 하면 실제 페이지 번호를 건너뛰게 되어 정확한 탐색 횟수를 계산할 수 없다.
    # 탐색횟수를 찾ㅈ는게아니라면 상관 X
    
import sys
sys.stdin = open("./input.txt", "r") # 이렇게하면 안에있는 인풋파일로 불러올수있음
'''

# 특별한 정렬 (max와 min활용)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     result = []
#
#     while len(nums) > 0:
#         max_v = max(nums)
#         ''' max_v 못쓰면?
#         max_v = float('-inf') # 음의 무한대
#         for i inr range(len(nums)):
#             if nums[i] > max_v:
#                 max_v = nums[i]
#         '''
#         nums.remove(max_v)
#         result.append(max_v)
#
#         min_v = min(nums)
#         nums.remove(min_v)
#         result.append(min_v)
#     print(f'#{tc}', *result[:10])

# 특별한 정렬 정렬로 푸는법
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    result = []
    lst_f, lst_b = [], []

    for i in range(len(nums)):
        if i < (len(nums) //2): # 앞부분은 lst_a에 추가
            lst_f.append(nums[i])
        elif i > (len(nums) //2) -1: # 뒷부분 은 lst_b에추가
            lst_b.append(nums[i])
        lst_b.sort(reverse=True)

    for i in range(5):
        result.append(lst_b[i])
        result.append(lst_f[i])

    print(f'#{tc}', *result)
'''
# 츄러스

N, K = map(int,input().split())
arr= list(int(input()) for _ in range(N))
start = 0
end = max(arr)

while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for l in arr: # 현재 mid 길이로 츄러스를 잘라 만들수 있는 츄러스의 개수 총합
        cnt += l //middle
    if cnt >= K:
        start = middle + 1
    else:
        end = middle - 1
print(end)