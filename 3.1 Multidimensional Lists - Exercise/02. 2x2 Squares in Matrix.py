row, col = [int(x) for x in input().split()]
matrix = []
count_square = 0

for _ in range(row):
    matrix.append(input().split())

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        if matrix[row][col] == matrix[row][col + 1] ==  matrix[row + 1][col] == matrix[row + 1][col + 1]:
            count_square += 1

print(count_square)
