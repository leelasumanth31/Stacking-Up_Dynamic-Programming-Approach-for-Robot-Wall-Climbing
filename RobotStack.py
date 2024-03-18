import sys

def fillMatrix(row_idx, col_idx, matrix, current_robot, max_size):

    if col_idx >= -1 and row_idx == current_robot:
        return 1
    if (row_idx > current_robot) or (col_idx < 0 ):
        return 0

    if matrix[row_idx][col_idx] != -1:
        return matrix[row_idx][col_idx]

    matrix[row_idx][col_idx] = 0

    for i in range(0, max_size + 1):
        matrix[row_idx][col_idx] += fillMatrix(row_idx + i, col_idx - 1, matrix, current_robot, max_size)

    return matrix[row_idx][col_idx]



with open(sys.argv[1], 'r') as file:

    for line in file:
        line = line.strip("\n")

        matrix = [
              [-1 for _ in range(0, 1004)] 
                for _ in range(0, 1004)
              ]

        b , n , k = tuple( map(int , line.split(" ") ))
        
        result = fillMatrix(0, n - 1, matrix, b, k)
        
        print(f'({b},{n},{k}) = {result}')