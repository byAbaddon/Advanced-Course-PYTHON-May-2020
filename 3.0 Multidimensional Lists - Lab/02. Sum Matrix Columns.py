row, col = [int(x) for x in input().split(', ')]
matrix = []
index = 0

for _ in range(row):
    matrix.append([int(x) for x in input().split()])


while True:
    matrix_col_sum = 0
    for i in range(len(matrix)):
        matrix_col_sum += matrix[i][index]
    
    print(matrix_col_sum)
    index += 1  

    if index == col:
        break