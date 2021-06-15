size_matrix = int(input())
matrix = []
diagonal_sum = 0

for _ in range(size_matrix):
    matrix.append([int(x) for x in input().split()])

index = 0
for row in matrix:
    diagonal_sum += row[index]    
    index += 1

print(diagonal_sum)