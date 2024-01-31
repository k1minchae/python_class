from itertools import permutations
import copy

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 풍선 개수, 총알 개수
    lst = list(map(int, input().split())) # 풍선 점수
    N_lst = []
    for i in range(N):
        N_lst.append(i)
    # 모든 경우의수 = N! -> 2차원리스트로 만들기 -> 순회 -> 점수계산
    # 모든 경우의 수를 담은 리스트 (행: N팩토리얼, 열: N)
    all_cases = list(permutations(N_lst))
    case_list = [list(permutation) for permutation in all_cases]

    score_list = []
    for i in case_list:
        score = 0   # 행 1개당 점수 초기화
        arr = copy.deepcopy(lst)

        for j in i:
            if (1 <= j < len(arr)-1) and (arr[j-1] != 0) and (arr[j+1] != 0): # 양쪽 터짐
                score += arr[j-1] * arr[j+1]
                arr.pop(j)
            if (j == 0 and arr[j+1] != 0) or (j+1 <= len(arr)-1 and arr[j+1] != 0 and arr[j-1] ==0): # 오른쪽만 터짐
                score += arr[j + 1]
                arr.pop(j)
            if (j == len(arr)-1 and arr[j-1] != 0) or (len(arr)-1 >= 0 and arr[j-1] != 0 and arr[j+1] == 0): # 왼쪽만 터짐
                score += arr[j-1]
                arr.pop(j)
            if (j==0 and arr[j+1]==0) or (j==len(arr)-1 and arr[j-1]==0) or (j != len(arr)-1 and arr[j+1] == 0 and arr[j-1]==0): # 자신만 터짐
                score += arr[j]
                arr.pop(j)

        score_list.append(score)
    print(max(score_list))