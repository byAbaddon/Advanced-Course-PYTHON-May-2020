matrix_size = int(input())
left, right = 0, 0

for i in  range(matrix_size):
    row = [int(x) for x in input().split()]
    left += row[i]
    right += row[len(row) - 1 - i]

print(abs(left -right))