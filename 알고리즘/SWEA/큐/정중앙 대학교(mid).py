import heapq
N = int(input())

big = []
small = []

mid = 500

def f(x):
    if mid > x:
        heapq.heappush(small, -x)
    elif mid < x:
        heapq.heappush(big, x)

for _ in range(N):
    a, b = map(int, input().split())
    f(a)
    f(b)

    if len(small) > len(big):
        heapq.heappush(big, mid)
        mid = - (heapq.heappop(small))

    elif len(big) > len(small):
        heapq.heappush(small, -mid)
        mid = heapq.heappop(big)

    print(mid)

# 정중앙 대학교
# import heapq
#
# lheap = []  # min heap
# rheap = []  # max heap
# mid = 500
#
# def push(v):
#     if mid > v:
#         heapq.heappush(lheap, -v)  # min heap
#     else:
#         heapq.heappush(rheap, v)   # max heap
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
#         mid = -heapq.heappop(lheap)
#     elif len(lheap) < len(rheap):
#         heapq.heappush(lheap, -mid)
#         mid = heapq.heappop(rheap)
#
#     print(mid)