# 아래 함수를 수정하시오.
new_list = []
def get_keys_from_dict(dict):
    
    for i in dict.keys():
        new_list.append(i)
    
    return new_list


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
