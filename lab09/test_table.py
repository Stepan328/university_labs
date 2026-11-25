from table import row_sums, column_sums, transform, diagonal_pattern, factorial, factorial_iterative


assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]


assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]


assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

#Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

#Узор размера 3x3
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

#Индивидуальный вариант (Вариант 15: ненулевые элементы заменить знаком: 1 или -1)
control_matrix = [[-2, 0, 3], [4, -5, 6]]
expected_result = [[-1, 0, 1], [1, -1, 1]]
assert transform(control_matrix) == expected_result

#Неизменяемость после преобразования
result = transform(control_matrix)
result[0][0] = 999
assert control_matrix[0][0] == -2

#Дополнительное задание
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(5) == factorial_iterative(5) == 120

print("Все проверки пройдены")
