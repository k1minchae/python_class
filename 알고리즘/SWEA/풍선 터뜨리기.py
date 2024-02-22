# 풍선 터뜨리기
def balloon(x, score=0):
    global max_score
    if len(x) == 2:
        max_score = max(score, max_score)
        return
    for i in range(1, len(x) - 1):
        new_score = score + x[i - 1] * x[i + 1]
        if x[i-1] == 1 and x[i+1] == 1:
            new_score = x[i] + score
        temp = x[i]  # 현재 풍선 값 저장
        del x[i]  # 터뜨리기
        balloon(x, new_score)
        x.insert(i, temp)  # 풍선 복구
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    max_score = 0
    arr = [1] + list(map(int, input().split())) + [1]
    balloon(arr)
    print(f'#{tc} {max_score}')