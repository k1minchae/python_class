import sys  # input() 쓰면 시간초과 될 수 있다.

vowels = ['a', 'e', 'i', 'o', 'u']


while True:
    english = sys.stdin.readline().lower()  # input값 받기 -> 소문자로.
    count_vowel = []    # while 이 한번돌 때마다 초기화되게
    if english == '#\n':    # sys.stdin.readline 라이브러리는 끝에 무조건 \n이 붙음
        break   # 샾을 발견하면 break (종료조건)
    else:
        for vowel in vowels:
            count_vowel.append(english.count(vowel))

    print(sum(count_vowel)) # 입력받은 문장마다 모음 개수 출력
