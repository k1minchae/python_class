# 다비치 민코드
# from itertools import combinations
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# M_arr = list(combinations(arr, M))
# min_v = float('inf')
# result = ()
# for i in M_arr:
#     cal = 1
#     for j in i:
#         cal *= j
#     if cal < min_v:
#         min_v = cal
#         result = i
# result = sorted(result)
# print(*result)
def cards(M, level=0, sum_v=1, sequence=[], used=set()):
    global min_v

    if level == M:
        if sum_v < min_v:
            min_v = sum_v
            return sequence
        else:
            return None

    min_sequence = None
    for num in arr:
        if num not in used:
            new_sum_v = sum_v * num
            new_sequence = sequence + [num]
            new_level = level + 1
            new_used = used.copy()
            new_used.add(num)

            result = cards(M, new_level, new_sum_v, new_sequence, new_used)
            if result is not None:
                min_sequence = result

    return min_sequence


N, M = map(int, input().split())
arr = list(map(int, input().split()))

min_v = float('inf')
result = cards(M)
print(*result)
