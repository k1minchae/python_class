T = int(input())
for tc in range(1, T+1):
    one_x1, one_y1, one_x2, one_y2 = map(int, input().split())
    two_x1, two_y1, two_x2, two_y2 = map(int, input().split())

    # 1번 상태
    if one_x1 < two_x1 < one_x2 or one_x1 < two_x2 < one_x2:
        if one_y1 < two_y1 < one_y2 or one_y1 < two_y2 < one_y2:
            result = 1

    # 2번 상태 (x축이 겹친다)
    elif one_x1 < two_x1 < one_x2 or one_x1 < two_x2 < one_x2:
        if one_y1 == two_y2 or two_y1 == one_y2:
            result = 2

    # 2번 상태 (y축이 겹친다)
    elif one_y1 < two_y1 < one_y2 or one_y1 < two_y2 < one_y2:
        if one_x1 == two_x2 or two_x1 == one_x2:
            result = 2

    # 4번 상태 (아예 안겹친다)
    elif (one_x2 < two_x1 or two_x2 < one_x1) or (one_y1 > two_y2 or two_y1 > one_y2):
        result = 4

    else: # 3번 상태
        result = 3

    print(f'#{tc} {result}')


# 강사님 코드
T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 1001 for _ in range(1001)]
    cnt = [0] * 5
    for _ in range(2):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(y1, y2+1):   # 사각형 테두리 또는 사각형의 내부
            for k in range(x1, x2+1)
                if j == y1 or j == y2 or k == x1 or k == x2:
                    arr[j][k] += 1 # 테두리 처리
                arr[j][k] += 1  # 내부 처리
                cnt[arr[j][k]] += 1 # 각 영역의 카운트 업데이트

    if cnt[4] == 1: # 4번 상태가 1번 나오면
        ans = 3
    elif cnt[4] > 1 and cnt[3] > 0:
        ans = 1
    elif cnt[4] > 1:
        ans = 2
    else:
        ans = 4
    print(f'#{tc} {ans}')