# import heapq
#
# q = []
#
# heapq.heappush(q, 1)
# heapq.heappush(q, 7)
# heapq.heappush(q, 3)
# heapq.heappush(q, 4)
#
# print(q)    # [1, 3, 4, 7] : 우선순위 대로 추가됨
#
# ans1 = heapq.heappop(q)
# ans2 = heapq.heappop(q)
#
# print(ans1) # 1
# print(ans2) # 3

# 정중앙 대학교
# import heapq
# lheap = [] # max heap
# rheap = [] # min heap
# mid = 500
#
# def push(v):
#     if mid > v:
#         heapq.heappush(lheap, -v)   # max heap 구현을 위해 -1곱해줌
#     else:
#         heapq.heappush(rheap, v)
#
# n = int(input())
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     push(a)
#     push(b)
#
#     if len(lheap) > len(rheap):
#         heapq.heappush(rheap, mid)
#         mid = -heapq.heappop(lheap) # max heap 에서 꺼낼때 -1 곱해줌
#     elif len(lheap) < len(rheap):
#         heapq.heappush(lheap, -mid) # max heap 에 값을 넣을 때 -1 곱해줌
#         mid = heapq.heappop(rheap)
#
#     print(mid)
#
# # ugly number
#
# import heapq
# N = int(input())
# K = list(map(int, input().split()))
# ugly = [] #어글리 넘버 저장할 리스트
# heap = [1] #최초 힙에 1을 넣음
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 5)
#
# while len(ugly) < max(K):
#     n = heapq.heappop(heap) #힙에서 최소값 가져오기
#     if n not in ugly: #중복 피하기
#         ugly.append(n)
#         heapq.heappush(heap, n * 2)
#         heapq.heappush(heap, n * 3)
#         heapq.heappush(heap, n * 5)
# for i in K:
#     print(ugly[i - 1], end = ' ')