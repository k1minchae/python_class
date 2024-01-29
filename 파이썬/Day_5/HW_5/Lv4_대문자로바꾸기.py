''' 문제
주어진 문자열에서 모든 단어의 첫 글자를 대문자로 변경하는 함수 작성
문자열을 인자로 받아 모든 단어의 첫글자를 대문자로 변경한 문자열 반환
'''

# 아래 함수를 수정하시오.
def capitalize_words(words):
    capital_word = words.title()
    return capital_word
result = capitalize_words("hello, world!")
print(result)
