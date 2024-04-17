# 다각형의 면적
import sys
input = sys.stdin.readline
N = int(input()) # N각형
arr = []
for _ in range(N):
    x = tuple(map(int, input().split()))
    arr.append(x)
arr += [(arr[0])] # 신발끈공식 편하게쓰려고 첫번째 값 끝에 추가해줌

temp1 = 0
temp2 = 0
# 현범이가 알려준 신발끈공식 쓰니깐 됨 ㅎㅎ
for i in range(len(arr)-1):
    temp1 += arr[i][0] * arr[i+1][1]
    temp2 += arr[i][1] * arr[i+1][0]
result = abs(temp1 - temp2)/2
print(round(result, 1))