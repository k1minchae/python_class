############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def get_final_position(N, matrix, move_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                x, y = row, col        
    
    for M in move_list:
        if M == 0:
            if 0 <= x <= 2:
                x = x - 1
            else: 
                return None
        elif M == 1:
            if 0 <= x <= 2:
                x = x + 1
            else:
                return None
        elif M == 2:
            if 0 <= y <= 2:
                y = y - 1
            else:
                return None
        elif M == 3:
            if 0 <= y <= 2:
                y = y + 1
            else:
                return None
    return [x, y]

''' 강사님 풀이
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
row = 0
col = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] ==1:
            row = i
            col = j
            break
            
for move in move_list:
    row += d_row[move]
    col += d_col[move]
    if row <= 0 or row >= N or col <0 or col >= N
        return None
    else:
        return [row, col]
'''

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
