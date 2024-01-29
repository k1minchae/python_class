'''
딕셔너리와 키, 값의 쌍을 인자로 받아 항목을 추가한 새로운 딕셔너리 반환
'''

# 아래 함수를 수정하시오.
dictionary = {}
def add_item_to_dict(dict, key, value):
    new_dict = dictionary.copy()
    new_dict.update(dict)
    new_dict.setdefault(key, value)

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

