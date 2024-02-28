# 베이비진 게임
from itertools import combinations

T = int(input())

def babygin(arr):
    for subset in combinations(arr, 3):
        if len(set(subset)) == 1:
            return True  # 모두 같은 숫자인 경우
        sorted_subset = sorted(subset)
        if sorted_subset[0] + 1 == sorted_subset[1] and sorted_subset[1] + 1 == sorted_subset[2]:
            return True  # 연속된 숫자인 경우
    return False  # 아님

for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    p_1 = []    # 플레이어 1
    p_2 = []    # 플레이어 2

    def f():
        for i in range(12):
            if i % 2:
                p_2.append(temp[i])
            else:
                p_1.append(temp[i])
            if len(p_1) >= 3:  # 카드 3개 골랐을 때부터 판별
                if babygin(p_1):
                    return 1
            if len(p_2) >= 3:
                if babygin(p_2):
                    return 2
        return 0

    print(f'#{tc} {f()}')


# 강사님 코드
def baby_gin(cards):
    cnt = [0] * 10 # 각 숫자별 카드 개수 저장
    for num in cards:
        cnt[num] += 1

    if 3 in cnt: # Triplet
        return True

    for i in range(8):  # Run
        if 0 not in cnt[i:i+3]:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    all_cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0

    for i in range(6):
        p1.append(all_cards[i*2])   # 플레이어 1의 카드
        if len(p1) > 2 and baby_gin(p1): # 카드가 3장 이상일 때 확인
            winner = 1
            break
        p2.append(all_cards[i * 2 + 1])
        if len(p2) > 2 and baby_gin(p2):
            winner = 2
            break
    print(f'#{tc} {winner}')