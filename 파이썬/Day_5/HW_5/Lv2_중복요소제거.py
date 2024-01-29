'''
주어진 리스트에서 중복된 요소를 제거한 새로운 리스트를 반환하는 함수작성
리스트를 인자로 받아 중복이 제거된 새로운 리스트 반환
'''

# 아래 함수를 수정하시오.
def remove_duplicates(list):
    for i in list:
        while list.count(i) > 1:
            list.remove(i)
    return list

result = remove_duplicates([1, 2, 2, 2, 3, 4, 4, 5])
print(result)
