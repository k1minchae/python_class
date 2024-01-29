'''
주어진 튜플을 정렬하여 새로운 튜플로 반환하는 sort_tuple 함수를 작성하시오
튜플을 인자로 받아 정렬된 새로운 튜플 반환

실행 결과 : (1, 2, 3, 5, 8)
'''

# 아래 함수를 수정하시오.

def sort_tuple(unsorted_tuple):
    return tuple(sorted(unsorted_tuple))
    

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
