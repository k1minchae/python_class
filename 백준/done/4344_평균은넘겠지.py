import sys

C = int(input()) # 테스트 케이스 개수

def average_value(sum_value, div_value): # 평균값 구하는 함수
    return sum_value / div_value

for _ in range(C):  
    count_average = 0

    # score = [학생수, 학생1점수, 학생2점수, ...]
    score = list(map(int, sys.stdin.readline().split()))

    # 학생들 점수평균
    avg = average_value(sum(score[1:]), score[0]) 

    # 학생들 점수를 순회하여 평균보다 높은지 확인
    for i in score[1:]: # score[0] 은 학생수이므로 slicing
        if i > avg:
            count_average += 1 # 높다면 +1


    print(f'{round((count_average / score[0]) * 100 , 3)}%')
    