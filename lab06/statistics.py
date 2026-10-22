digits = list(map(int, input("Введите целые числа через пробел: ").split()))
if len(digits) == 0:
    print("Нет данных")
else:
    min_chis = digits[0]
    max_chis = digits[0]
    for chis in digits:
        if chis < min_chis:
            min_chis = chis
        elif chis > max_chis:
            max_chis = chis
    print(f"Количество: {len(digits)} | Сумма: {sum(digits)}\n"
          f"Минимум: {min_chis} | Максимум: {max_chis}\n"
          f"Среднее арифметическое: {(sum(digits) / len(digits)):.2f}")
