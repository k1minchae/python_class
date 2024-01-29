list = list(map(int, input().split()))

if sorted(list) == list:
    print('ascending')
    
    # 내림차순
elif sorted(list, reverse=True) == list:
    print('descending')
else:
    print('mixed')