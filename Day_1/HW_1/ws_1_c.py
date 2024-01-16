"""
총 5개의 글자를 password 문장에서 찾아서 각각의 변수에 할당해야함.

first_char 변수에 할당할 글자는 
password 문자열의 28번째부터 35번째까지에 작성된 글자

second_word 변수에 할당할 단어는
113번째부터 총 5글자

third_word 변수에 할당할 단어는
66번째부터 68번째까지 작성된 글자를 뒤집어서

fourth_word 변수에 할당할 단어는
322번째부터 총 4글자를 뒤집어서 출력

fifth_word 변수에 할당할 단어는
365번째부터 작성된 python 이다.

f-string 을 활용하여 출력하시오.
이때 각 n번째는 문자열의 index 값을 의미한다.
"""

# password 변수는 주어짐
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."

# password를 활용하여 각각 변수를 만드시오.
first_char = password[28:36]
second_word = password[113:118]
third_word = password[66:69]
fourth_word = password[322:326]
fifth_word = password[365:372]

print(f'{first_char}{second_word} {third_word[::-1]} {fourth_word[::-1]} {fifth_word}')