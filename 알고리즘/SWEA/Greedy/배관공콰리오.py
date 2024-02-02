N, L = map(int, input().split())  # N: 물이 세는곳 개수 // L: 테이프 길이
arr = list(map(int, input().split())) # 물 세는곳 위치
arr.sort()

cnt = 1 # 첫 번째 구멍에 테이프 붙이고 시작
start = arr[0]

# 두 번째 구멍부터 탐색
for i in range(1, N):
    # 현재 테이프로 구멍을 막을 수 있다면
    if arr[i] - start < L:  # 다음 구멍까지의 거리가 테이프의 길이보다 작으면
        continue
    else:  # 못 막으면 테이프 붙이고 count += 1
        start = arr[i]
        cnt += 1

print(cnt)






# 시간초과 코드
# while arr:
#     for i in range(0, len(arr)-1):
#         for l in range(L, 0, -1):
#             for j in range(i+1, len(arr)):
#                 if arr[j] - arr[i] == l:
#                     cnt += 1
#                     del arr[i:j+1]
#                     break
#             else:
#                 continue
#
#             break
# print(cnt)