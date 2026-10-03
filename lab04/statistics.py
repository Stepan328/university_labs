n = int(input("Введите число: "))
sum_numbers = 0
count_positive = 0
maximum = -10**1000
count = 1
for i in range(n):
    chis = int(input(f"Введите число номер {count}: "))
    sum_numbers += chis
    if chis > 0:
        count_positive += 1
    if chis > maximum:
        maximum = chis
    count += 1
print(f"Сумма чисел: {sum_numbers}; количество положительных значений: {count_positive}; "
      f"максимальное значение: {maximum}")
