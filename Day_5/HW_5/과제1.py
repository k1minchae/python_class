# 아래 함수를 수정하시오.
text_list = []
def count_character(message, x):
    for i in message:
        text_list.append(i)
    count_x = text_list.count(x)
    return count_x

result = count_character("Hello, World!", "o")
print(result)  # 2
