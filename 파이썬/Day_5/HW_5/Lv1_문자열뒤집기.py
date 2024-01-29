'''문제
주어진 문자열을 역순으로 반환하는 함수 작성
주어진 문자열을 인자로 받아 역순으로 된 문자열 반환
슬라이싱 사용하지 말기. built-in function reversed사용

실행결과 : !dlroW ,olleH
'''
# 아래 함수를 수정하시오.
text_list = []
def reverse_string(message):
    for i in message:
        text_list.append(i)
    text_list.reverse()
    text = ''.join(text_list)
    return text

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
