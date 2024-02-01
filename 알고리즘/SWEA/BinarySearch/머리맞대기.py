import pprint
import itertools
N, T = map(int, input().split())
arr = list(map(int, input().split()))

n = len(arr)

arr_list = []
for i in range(1<<n):
    lst = []
    for j in range(n):
        if i & (1<<j):
            lst.append(arr[j])
    if len(lst) == 3:
        arr_list.append(lst)

five_list = []
for i in arr_list:
    five_list.append(set(arr) - set(i))

pprint.pprint(five_list)
# result_list = []
# compare_list_3 = []
# compare_list_2 = []
# compare = set(compare_list_3) + set(compare_list_2)
# for i in arr_list:
#     compare_list_3.append(set(itertools.combinations(list(set(arr) - set(i)), 3)))
#
# for i in arr_list:
#     compare_list_2.append(())
# for i in arr_list:
#     for j in compare:
#         if sum(i) >= sum(j):
#             result_list.append(sum(i))
#
# print(min(result_list))