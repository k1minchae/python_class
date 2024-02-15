# 토너먼트 카드게임
# def binary_divide(arr):
#     global temp
#     if len(arr) <= 2:  # 카드가 2장 이하인 경우
#         return rcp(*arr)
#     mid = (len(arr)-1) // 2
#     binary_divide(arr[:mid+1])  # 왼쪽 부분 배열에 대해 이진 탐색 호출
#     binary_divide(arr[mid+1:])  # 오른쪽 부분 배열에 대해 이진 탐색 호출
#     return
# def rcp(a, b=(0, 0)):
#     if a[1] == b[1] or (b[1] == 3 and a[1] == 1):
#         return a[0]
#     elif a[1] > b[1] and not (a[1] == 3 and b[1] ==1):
#         return a[0]
#     else:
#         return b[0]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [(idx+1, val) for idx, val in enumerate(list(map(int, input().split())))]
#     temp = []
#     result = binary_divide(arr)  # 이진 탐색 호출
#     print(result)
def rcp(a, b):
    if arr[a] == arr[b] or (arr[a] == 1 and arr[b] ==3):
        return a
    elif arr[b] < arr[a] and not (arr[b] == 1 and arr[a] == 3):
        return a
    else:
        return b

def div(s, e):
    mid = (s + e) // 2
    if s == e:   # 한 명 남으면 부전승
        return s
    team_a = div(s, mid)
    team_b = div(mid+1, e)
    return rcp(team_a,team_b)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = div(0,N-1) + 1
    print(f'#{tc} {result}')