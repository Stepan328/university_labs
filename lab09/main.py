from table import row_sums, column_sums, diagonal_pattern, transform


rows = int(input("Введите количество строк в таблице: "))
while rows <= 0:
    rows = int(input("Данные введены некорректно. Введите количество строк (положительное число): "))

columns = int(input("Введите количество столбцов в таблице: "))
while columns <= 0:
    columns = int(input("Данные введены некорректно. Введите количество столбцов (положительное число): "))

table = [[0 for _ in range(columns)] for _ in range(rows)]
for i in range(rows):
    row = input(f"Введите {i+1} строку через пробел ({columns} значений): ").split()
    while len(row) != columns:
        row = input(f"Данные введены некорректно. Нужно ровно {columns} чисел. Повторите {i+1} строку: ").split()
    table[i] = list(map(int, row))

print("\n--- Исходная таблица ---")
for r in table:
    print(*r)

snapshot = [row.copy() for row in table]
print(f"\nСумма строк: {row_sums(table)}")
print(f"Сумма столбцов: {column_sums(table)}")
assert snapshot == table

# --- Индивидуальный вариант №15 ---
print("\n--- Преобразованная таблица (ненулевые элементы заменить знаком: 1 или -1) ---")
transformed = transform(table)
for r in transformed:
    print(*r)

# --- Диагональный узор ---
print()
size = int(input("Введите размер квадратной матрицы (положительное число): "))
while size <= 0:
    size = int(input("Данные введены некорректно. Введите положительный размер: "))

print("--- Диагональный узор ---")
pattern = diagonal_pattern(size)
for r in pattern:
    print(*r)
