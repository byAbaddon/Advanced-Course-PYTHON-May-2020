import sys

size_matrix = int(input())
matrix = []

for _ in range(size_matrix):
    matrix.append(input())

symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol: 
            print((row,col))
            sys.exit()

print(symbol, 'does not occur in the matrix')
