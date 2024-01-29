'''
주어진 셋을 인자로 받아 합집합 반환
'''
# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    union_set = set1.union(set2)
    return union_set 


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
