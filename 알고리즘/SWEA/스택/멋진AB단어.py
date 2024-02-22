N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    def AB_word(word):
        stack = []
        global cnt
        if len(word) % 2 != 0: # 홀수면 중단
            return 0
        if len(word) == 2 and word[0] != word[1]: # 단어가 2개일 때 서로 다르면 중단
            return 0
        for w in word:
            if len(stack) == 0:  # 스택이 비어있을 때 단어 추가
                stack.append(w)
            elif len(stack) == 1 and stack[0] != w:
                stack.append(w)
            else:
                if stack.pop() != w:
                    return 0
        if stack == []:
            cnt += 1
    AB_word(word)
print(cnt)