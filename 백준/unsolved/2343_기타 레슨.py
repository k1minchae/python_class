# 기타 레슨
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

def Blue(arr, target):
    s = max(arr) # 가장 긴 강의가 들어갈 수 있도록 시작값 설정
    e = sum(arr) # 블루레이의 최대값
    while s <= e:
        mid = (s + e) // 2 # 블루레이 용량 설정
        total = 0 # 현재 블루레이에 넣은 길이
        count = 1 # 블루레이의 개수

        # 배열 순회하며 누적합 구하기
        for num in arr:
            total += num

            # 용량 초과
            if total > mid:
                count += 1 # 블루레이 추가
                total = num # 새로운 블루레이에 현재 값 저장

        if count <= target: # 블루레이 개수 더 늘려도 되는 경우
            e = mid - 1 # 블루레이 용량 줄임

        else:   # 블루레이 개수 줄여야 하는 경우
            s = mid + 1 # 블루레이 용량 늘림
    return s    # 최적의 블루레이

print(Blue(arr, M))