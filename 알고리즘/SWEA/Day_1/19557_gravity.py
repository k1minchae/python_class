def gravity(boxes):
    max_v = 0
    for idx, box in enumerate(boxes): # 인덱스와 요소를 저장하는 함수
        count = 0
        for next in range(idx + 1, N): # N은 가로 길이
            if box > boxes[next]:
                count += 1
        max_v = max(max_v, count)
    return max_v

T = int(input())  # 테스트 케이스의 개수
for tc in range(1, T+1):
    N = int(input())  # 방의 가로 길이
    boxes = list(map(int, input().split()))
    result = gravity(boxes) # 함수 호출하는데에서 중단점 잡기
    print(f'#{tc} {result}')
