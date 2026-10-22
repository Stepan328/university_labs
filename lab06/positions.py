digits = list(map(int, input("Введите целые числа через пробел: ").split()))
if len(digits) > 0:
    max_chis = max(digits)
    index = [chis for chis, i in enumerate(digits) if digits[chis] == max_chis]
    print(f"Индексы максимального элемента: {index}")
else:
    print("Нет данных")
