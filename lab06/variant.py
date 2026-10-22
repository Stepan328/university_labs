chisla= input("Введите целые числа через пробел: ").split()
digits = [int(chis) for chis in chisla if abs(int(chis)) % 10 == 2]
print(f"Исходный список: {digits} | Количество: {len(digits)} | Сумма: {sum(digits)} | Отсортированная по возрастанию копия: {sorted(digits)}")
