row, col = [ int(x) for x in input().split(', ')]
matrix = []
matrix_sum = 0

for i in range(row):
    matrix.append([int(x) for x in input().split(', ')])
    matrix_sum += sum(matrix[i])

print(matrix_sum)
print(matrix)