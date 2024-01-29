'''
중복된거 제거하고 set로 변환
리스트를 인자로 받아서 set 반환 하자
'''

# 아래 함수를 수정하시오.
my_set = set()
def remove_duplicates_to_set(list):
    my_set.update(list)
    return my_set

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
