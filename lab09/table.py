def row_sums(matrix):
    total = []
    for row in matrix:
        total.append(sum(row))
    return total


def column_sums(matrix):
    if not matrix:
        return []
    total = [0 for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for row in matrix:
            total[i] += row[i]
    return total


def diagonal_pattern(size):
    total = [[0 for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(size):
            if row == column:
                total[row][column] = 0
            elif row < column:
                total[row][column] = 1
            else:
                total[row][column] = 2
    return total

def transform(matrix):
    if not matrix:
        return []
    total = [r.copy() for r in matrix]
    rows_len = len(total[0])
    for row in range(len(total)):
        for column in range(rows_len):
            if total[row][column]  != 0:
                if total[row][column] < 0:
                    total[row][column] = -1
                if total[row][column] > 0:
                    total[row][column] = 1
    return total

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

def factorial_iterative(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
