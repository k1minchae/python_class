"""
주어진 문자열을 적절한 변수에 할당하여 
예시 화면과 동일하게 출력될 수 있도록 코드를 작성하시오.

예시
반짝 반짝 작은 별 아름답게 비치네
동쪽 하늘에서도 서쪽 하늘에서도
반짝 반짝 작은 별 아름답게 비치네
"""


twinkle = '반짝 반짝'
in_the = '에서도'
little_star = '작은 별'
beautiful = '아름답게 비치네'
east_sky = '동쪽 하늘'
west_sky = '서쪽 하늘'

print(twinkle, little_star, beautiful)
print(f'{east_sky}{in_the} {west_sky}{in_the}')
print(twinkle, little_star, beautiful)