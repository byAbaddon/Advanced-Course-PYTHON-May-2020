row, col = [int(x) for x in input().split(', ')]
matrix = []
square_matrix = [[0, 0], [0, 0]]


for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) -1 ):
        square_matrix_sum = square_matrix[0][0] + square_matrix[0][1] + square_matrix[1][0] + square_matrix[1][1]
        big_square_sum = matrix[row][col] + matrix[row][col + 1] +  matrix[row + 1][col] + matrix[row + 1][col + 1]

        if big_square_sum > square_matrix_sum: 
            square_matrix = [ [matrix[row][col],  matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

square_sum = 0
for row in square_matrix:
    print(*row)
    square_sum += row[0] + row[1] 

print(square_sum)
 

           
           



