
## LU분해를 할 matrix 입력받기
def get_matrix_input():
    
    matrix = []

    for i in range(1,4):
        row = list(map(float,input(f"{i}번째 행의 요소를 공백을 기준으로 넣어주세요.").split(" ")))
        matrix.append(row)
    print() # 줄바꿈

    return matrix


## 입력 받은 matrix 출력하기
def print_matrix(matrix,name = "입력 받은 행렬"):
    print("{0}:".format(name))
    print() #줄바꿈
    for row in range(3):
        print(matrix[row])
    print() # 줄바꿈

## LU 분해 초기값 설정
'''
     1 0 0          0 0 0
L =  0 1 0      U = 0 0 0
     0 0 1          0 0 0

'''

def initialize_LU():   # initialize_LU[0] = L , initialize_LU[1] = U
    L = [[0.0 for _ in range(3)] for _ in range(3)]
    U = [[0.0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):

            if i == j:
                L[i][j] = 1

    return [L,U] 
    


# matrix를 입력하면 LU 분해해서 결과를 내놓음 
def lu_decomposition(matrix):

    L = initialize_LU()[0]
    U = initialize_LU()[1]
    
    for i in range(3):
        for j in range(3):
            if (i == 0):            ## U의 첫번째 행은 입력받은 matrix의 첫행과 같음
                U[i][j] = matrix[i][j] 

            try:
                if (j == 0):
                    L[i][j] = matrix[i][j]/U[0][0]

            except ZeroDivisionError:
                print("입력한 행렬의 1,1 성분이 0 이라서 LU 분해 할 수 없습니다.")

            if (i == 1) and (j >= 1):
                U[i][j] = matrix[i][j] - L[i][0]*U[0][j]

            if (i == 2) and (j == 1):
                L[i][j] = (matrix[i][j] - L[i][0]*U[0][j]) / U[j][j]

            if (i == 2) and (j ==2 ):
                U[i][j] = matrix[i][j] - L[i][0]*U[0][j] - L[i][1]*U[1][j]
    return [L,U]

    '''
        1 0 0          x x x
    L = x 1 0      U = 0 x x
        x x 1          0 0 x
    '''



def main():
    matrix = get_matrix_input() # matrix 입력받기
    print_matrix(matrix)
    L = lu_decomposition(matrix)[0]
    U = lu_decomposition(matrix)[1]

    print_matrix(L, name= "L 출력")
    print_matrix(U ,name= "U 출력")




if __name__ == "__main__":
    main()

