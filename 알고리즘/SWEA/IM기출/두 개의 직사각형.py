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