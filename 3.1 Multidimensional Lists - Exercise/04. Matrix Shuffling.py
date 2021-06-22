rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    token = input().split()
    
    if len(token) == 1:
        break
    elif 'swap' not in token:
        print('Invalid input!')
    elif len(token) == 5:
        swap, row1, col1, row2, col2 = [int(x) if x.isdigit() else x for x in token]
        if row1 <= rows and row2 <= rows  and col1 <= cols  and col2 <= cols:
            first_change = matrix[row1][col1]
            second_change = matrix[row2][col2]
            matrix[row1][col1] = second_change
            matrix[row2][col2] = first_change

            for row in matrix:
                print(*row)

        else:
            print('Invalid input!')
    else:
        print('Invalid input!')