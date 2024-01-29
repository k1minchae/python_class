import sys

word = (str(sys.stdin.readline().strip('\n'))).upper()
count_word_dict = {}  # 각 문자의 등장 횟수를 저장할 딕셔너리

for char in word:
    # 딕셔너리에 문자가 등록되어 있으면 +1, 아니면 1로 초기화
    count_word_dict[char] = count_word_dict.get(char, 0) + 1

# 가장 많이 나온 첫 번째 단어
best_word = max(count_word_dict, key=count_word_dict.get)

# 가장 많이 나온 횟수
num_max = count_word_dict[best_word]

# 가장 많이 나온 횟수의 문자가 하나인지 확인
result = [char for char, count in count_word_dict.items() if count == num_max]

if len(result) == 1:
    print(result[0])
else:
    print('?')


