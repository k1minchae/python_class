# import copy
# n, m = map(int, input().split()) # 필요한 보드카 수 N  // 마트의 수 M
#
# result_prices = [] # 마트별 최소가격 리스트
# for _ in range(m):
#     N = copy.deepcopy(n)
#     M = copy.deepcopy(m)
#     set_p, one_p = map(int, input().split()) # 마트별 6세트가격 / 개당가격
#     if set_p > one_p * 6:
#         result_prices.append(N * one_p)
#     else:
#         price = 0
#         while N >= 1:
#             if N >= 6:
#                 price += set_p
#                 N -= 6
#             else:
#                 if N * one_p < set_p:
#                     price += N * one_p
#                     N = 0
#                 else:
#                     price += set_p
#                     N = 0
#         result_prices.append(price)
#
# print(min(result_prices))

# 종강파티
N, M = map(int, input().split()) # 필요한 보드카 수 N  // 마트의 수 M
six_min = float('inf')
one_min = float('inf')

for _ in range(M):
    six_cost, one_cost = map(int, input().split())
    six_min = min(six_min, six_cost)
    one_min = min(one_min, one_cost)

# 만약 낱개로 6명 사는게 // 세트로 6병 사는거보다 저렴하면 낱개로구매
if one_min * 6 < six_min:
    print(one_min * N)

else:
    buy = N //6 # 먼저 세트로 구매
    N %= 6 # 남은 병수

    # 남은 병수를 낱개로 사는게 더 비싸다면 세트가 더 싸니깐 세트로 구매
    if N * one_min > six_min:
        buy += 1
        print(buy * six_min)
    else: # 남은 병수를 낱개로 사는게 이득이면
        print(buy * six_min + one_min * N)
