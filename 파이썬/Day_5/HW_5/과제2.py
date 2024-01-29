# 아래 함수를 수정하시오.
def find_min_max(list):
    list.sort()
    max_list = list.pop()
    list.sort(reverse=True)
    min_list = list.pop()
    return (min_list, max_list)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
