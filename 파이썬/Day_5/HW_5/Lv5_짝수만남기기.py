''' 문제
주어진 리스트에서 홀수 모두 제거
짝수만을 남긴 리스트를 반환하는 함수 작성

단, extend 와 pop 사용해서 구현
'''

# 아래 함수를 수정하시오.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
result_list = []
def even_elements(lists):

    for i in lists:
        if i % 2 == 0:
            even_list.append(i)
    my_list.extend(even_list)

    for j in range(len(even_list)):
        even_numbers = my_list.pop()
        result_list.append(even_numbers)
    result_list.reverse()
    return result_list


result = even_elements(my_list)
print(result)

